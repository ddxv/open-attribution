"""
API endpoints for share links.

Any URL to /s/ will look up the data in the database
and then redirect to the landing page with the web SDK
that checks if the user has already installed the app.


Endpoints for Share Links
=========
GET /api/links/share/{share_slug:str}
POST /api/links/update

"""

import json
from enum import Enum
from typing import Self

import ua_parser
from config import IMPRESSION_CLICK_PRODUCER, get_logger
from config.dimensions import (
    DB_AD_ID,
    DB_AD_NAME,
    DB_C,
    DB_C_ID,
    DB_CITY_NAME,
    DB_CLIENT_IP,
    DB_COUNTRY_ISO,
    DB_IFA,
    DB_LINK_UID,
    DB_NETWORK,
    DB_RECEIVED_AT,
    DB_STATE_ISO,
    DB_STORE_ID,
)
from confluent_kafka import KafkaException
from dbcon.queries import STORE, update_app_links_store
from detect.geo import get_geo
from litestar import Controller, Request, get, post
from litestar.background_tasks import BackgroundTask
from litestar.exceptions import HTTPException
from litestar.response import Redirect

from api_app.tools import EMPTY_IFA, generate_link_uid, get_client_ip, now

logger = get_logger(__name__)


class OSID(Enum):
    """Enum for store IDs."""

    ANDROID = "android"
    IOS = "ios"
    WEB = "web"
    ERROR = "error"


def is_android_device(user_agent: str) -> bool:
    """Determine if the request is from an Android device."""
    try:
        parsed_ua = ua_parser.parse(user_agent)
        return parsed_ua.os.family.lower() == "android"
    except Exception:
        logger.exception("Error parsing user agent")
        return False


def is_ios_device(user_agent: str) -> bool:
    """Determine if the request is from an iOS device."""
    try:
        parsed_ua = ua_parser.parse(user_agent)
        return parsed_ua.os.family.lower() in {"ios", "iphone os"}
    except Exception:
        logger.exception("Error parsing user agent")
        return False


def get_redirect_url(
    link_data: dict,
    request: Request,
) -> tuple[str, str | None]:
    """Get the redirect URL and store ID based on the device type."""
    user_agent = request.headers.get("User-Agent", "")
    logger.info(f"User-Agent: {user_agent}")

    if is_android_device(user_agent):
        detected_os = OSID.ANDROID
        # Maybe all android devices should go to the market uri?
        if link_data["android_market_uri"]:
            redirect_url = link_data["android_market_uri"]
        else:
            redirect_url = link_data["web_redirect"]
        try:
            store_id = link_data["google_store_id"]
        except KeyError:
            store_id = None
    elif is_ios_device(user_agent):
        detected_os = OSID.IOS
        if link_data["apple_redirect"]:
            redirect_url = link_data["apple_redirect"]
        else:
            redirect_url = link_data["web_redirect"]
        try:
            store_id = link_data["apple_store_id"]
        except KeyError:
            store_id = None
    else:
        logger.info("No mobile OS detected!")
        detected_os = OSID.WEB
        if link_data["web_redirect"]:
            redirect_url = link_data["web_redirect"]
            if "play.google.com/store/apps/details?id=" in redirect_url:
                detected_os = OSID.ANDROID
                store_id = link_data["google_store_id"]
            elif "apps.apple.com/app/id" in redirect_url:
                detected_os = OSID.IOS
                store_id = link_data["apple_store_id"]
            else:
                store_id = None
        else:
            logger.error("No web redirect found!")
            redirect_url = "/"
            store_id = None
            detected_os = OSID.ERROR

    logger.info(f"Redirect URL: {redirect_url=} {detected_os=} {store_id=}")
    return redirect_url, store_id


async def process_as_click(
    link_data: dict,
    request: Request,
    store_id: str | None,
) -> None:
    """Process the share link in background."""
    client_host = get_client_ip(request)
    link_uid = generate_link_uid()

    event_time = now()
    ifa = EMPTY_IFA
    source = link_data.get("network_postback_id")
    c = link_data.get("campaign_name")
    c_id = link_data.get("campaign_id")
    ad = link_data.get("ad_name")
    ad_id = link_data.get("ad_id")

    geo_data = get_geo(client_host)
    country_iso = geo_data.get("country_iso")
    state_iso = geo_data.get("state_iso")
    city_name = geo_data.get("city_name")

    data = {
        "event_time": event_time,
        DB_NETWORK: source,
        DB_STORE_ID: store_id,
        DB_C: c,
        DB_C_ID: c_id,
        DB_AD_NAME: ad,
        DB_AD_ID: ad_id,
        DB_IFA: ifa,
        DB_CLIENT_IP: client_host,
        DB_LINK_UID: link_uid,
        DB_COUNTRY_ISO: country_iso,
        DB_STATE_ISO: state_iso,
        DB_CITY_NAME: city_name,
        DB_RECEIVED_AT: now(),
    }

    try:
        enc_data = json.dumps(data).encode("utf-8")
        IMPRESSION_CLICK_PRODUCER.produce("clicks", value=enc_data)
        IMPRESSION_CLICK_PRODUCER.poll(0)
    except KafkaException as ex:
        logger.exception("Write share to Kafka Clicks failed.")
        raise HTTPException(status_code=500, detail=ex.args[0].str()) from ex


class ShareController(Controller):
    """
    Recording for share endpoints.

    Endpoints for Share Links
    =========
    GET /api/links/share/{share_slug:str} (redirects to the store ID's URL based on the device type)
    POST /api/links/update (Refreshes the app links store based on app_links table in database)

    """

    path = "api/links"

    @get(path="share/{share_slug:str}")
    async def shared_link(
        self: Self,
        request: Request,
        share_slug: str,
    ) -> Redirect:
        """
        Redirect to the store ID's URL based on the device type.

        URL Path: GET api/links/share/{share_slug:str}

        Args:
        ----
            self: not for external use
            request: not for external use
            share_slug (str): The share slug included in the URL path.

        Returns:
        -------
        - Redirect: Redirects to the store ID's URL based on the device type.

        Behavior
        --------
        1. Determines the store ID to redirect to based on the device type.
        2. Redirects to the store ID's URL.
        3. Processes the share link in the background as a click event.

        Example Usage
        -------------
        ```
        GET https://track.example.com/s/abc
        ```

        """
        app_links = await STORE.get("app_links")

        if len(app_links) == 0:
            logger.error(
                f"Redirect links empty! Set share link on dashboard. No redirect found for {share_slug}",
            )
            # TODO: Attempts to redirect ot the root of the share url with possibly no landing page
            return Redirect(path="/")

        try:
            link_data = app_links[share_slug]
        except KeyError:
            logger.warning(f"No link associated with {share_slug}")
            return Redirect(path="/")

        redirect_url, store_id = get_redirect_url(
            link_data,
            request,
        )

        return Redirect(
            path=redirect_url,
            background=BackgroundTask(
                process_as_click,
                link_data,
                request,
                store_id,
            ),
        )

    @post(path="/update")
    async def update_links(self: Self) -> dict:
        """
        Update the app links store based on app_links table in database.

        Returns
        -------
        - None: The function does not return any value.

        """
        await update_app_links_store()
        return {"status": "success"}
