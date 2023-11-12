from api_app.controllers.postbacks import PostbackController
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig

import logging

from litestar.openapi import OpenAPIConfig, OpenAPIController

cors_config = CORSConfig(
    allow_origins=[
        "localhost",
    ]
)


class MyOpenAPIController(OpenAPIController):
    path = "/api/docs"


logging_config = LoggingConfig(
    root={"level": logging.getLevelName(logging.INFO), "handlers": ["console"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
)


app = Litestar(
    route_handlers=[PostbackController],
    cors_config=cors_config,
    openapi_config=OpenAPIConfig(
        title="App Store API", version="0.0.1", openapi_controller=MyOpenAPIController
    ),
    logging_config=logging_config,
    debug=True,
)
