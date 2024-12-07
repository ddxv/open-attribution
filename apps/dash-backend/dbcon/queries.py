"""Query database for backend API."""

import pathlib
from typing import cast

import pandas as pd
from config import MODULE_DIR, get_logger
from sqlalchemy import Engine, text

from dbcon.connections import get_db_connection

logger = get_logger(__name__)


SQL_DIR = pathlib.Path(MODULE_DIR, "dbcon/sql/")


def load_sql_file(file_name: str) -> str:
    """Load local SQL file based on file name."""
    file_path = pathlib.Path(SQL_DIR, file_name)
    with file_path.open() as file:
        mytxt: str = text(file.read())
        return mytxt


QUERY_NETWORKS = load_sql_file(
    "networks.sql",
)
INSERT_NETWORK = load_sql_file(
    "insert_network.sql",
)
DELETE_NETWORK = load_sql_file(
    "delete_network.sql",
)

QUERY_APPS = load_sql_file(
    "apps.sql",
)
QUERY_APP = load_sql_file(
    "app.sql",
)

INSERT_APP = load_sql_file(
    "insert_app.sql",
)
DELETE_APP = load_sql_file(
    "delete_app.sql",
)


def query_networks() -> pd.DataFrame:
    """Get all networks."""
    logger.info("Query all networks.")
    df = pd.read_sql(
        QUERY_NETWORKS,
        con=DBCON.engine,
    )
    return df


def insert_custom_network(network_name: str, postback_id:str ) -> None:
    """Insert a new network."""
    logger.info(f"Inserting new network: {network_name} {postback_id=}")

    with ENGINE.connect() as connection:
        connection.execute(
            INSERT_NETWORK,
            {"network_name": network_name, "status": "active", "postback_id": postback_id, "is_custom": True},
        )
        connection.commit()


def delete_network(network_id: int) -> None:
    """Delete custom network."""
    logger.info(f"Delete network: {network_id}")

    with ENGINE.connect() as connection:
        connection.execute(DELETE_NETWORK, {"network_id": network_id})
        connection.commit()


def query_apps(store_id: str | None = None) -> pd.DataFrame:
    """Get all apps or a single app."""
    logger.info(f"Query {'all' if store_id is None else f'app: {store_id}'} apps.")

    if store_id is None:
        df = pd.read_sql(
            QUERY_APPS,
            con=ENGINE,
        )
    else:
        df = pd.read_sql(
            QUERY_APP,
            params={"store_id": store_id},
            con=ENGINE,
        )
    return df


def insert_app(app_name: str, store_id: str, store: int) -> None:
    """Insert a new network."""
    logger.info(f"Inserting new app: {app_name}")

    with ENGINE.connect() as connection:
        connection.execute(
            INSERT_APP,
            {"app_name": app_name, "store_id": store_id, "store": store},
        )
        connection.commit()


def delete_app(app_id: int) -> None:
    """Delete custom network."""
    logger.info(f"Delete app: {app_id}")

    with ENGINE.connect() as connection:
        connection.execute(DELETE_NETWORK, {"app_id": app_id})
        connection.commit()


logger.info("set db engine")
DBCON = get_db_connection("admin-db")
DBCON.set_engine()

if DBCON.engine is None:
    msg = "DBCON.engine is None"
    logger.error(msg)
    raise ValueError(msg)

ENGINE = cast(Engine, DBCON.engine)
