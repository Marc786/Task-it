import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from task_api.config.context.application_context import ApplicationContext
from task_api.config.logger.logger import Logger
from task_api.config.service_locator import ServiceLocator
from task_api.core.account.api.account_resource import router as user_router
from task_api.exception.configuration_exception import ConfigurationException
from task_api.exception.invalid_input_exception import InvalidInputException
from task_api.exception.item_already_exists_exception import ItemAlreadyExistsException
from task_api.health import router as health_router
from task_api.http.handler.invalid_input_exception_handler import (
    invalid_input_exception_handler,
)
from task_api.http.handler.item_already_exists_exception_handler import (
    item_already_exists_exception_handler,
)
from task_api.http.handler.server_config_exception_handler import (
    server_config_exception_handler,
)
from task_api.http.handler.server_exception_handler import server_exception_handler

logger = Logger.get_logger()


def launch(app_context: ApplicationContext):
    app = setup_app(app_context)

    logger.info("Launching the application...")
    uvicorn.run(app, host=app_context.server_host, port=app_context.server_port)


def setup_app(app_context: ApplicationContext) -> FastAPI:
    logger.info("Building the application...")

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    add_exception_handlers(app)

    include_routers(app)

    app_context.initialize_dependencies()
    ServiceLocator.register_dependency(ApplicationContext, app_context)

    logger.info("Application built successfully")
    return app


def include_routers(app: FastAPI):
    app.include_router(health_router)
    app.include_router(user_router)


def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, server_exception_handler)
    app.add_exception_handler(ConfigurationException, server_config_exception_handler)
    app.add_exception_handler(InvalidInputException, invalid_input_exception_handler)
    app.add_exception_handler(
        ItemAlreadyExistsException, item_already_exists_exception_handler
    )
