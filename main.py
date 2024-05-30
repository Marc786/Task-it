import argparse

from task_api import app_launcher
from task_api.config.context.application_context import ApplicationContext, Environment
from task_api.config.context.development_context import DevelopmentContext
from task_api.config.context.production_context import ProductionContext
from task_api.config.logger import logger_type
from task_api.config.logger.logger import Logger

logger = Logger.get_logger()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env",
        dest="env",
        type=str,
        help="Environment to run in \n - dev \n - prod",
    )
    parser.add_argument(
        "--host",
        dest="host",
        type=str,
        help="Host to bind to",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        help="Port to bind to",
    )
    parser.add_argument(
        "--logging",
        dest="logging",
        default="json",
        type=str,
        help="Logging type : pretty, json",
    )
    return parser.parse_args()


def get_application_context(args: argparse.Namespace) -> ApplicationContext:
    if args.env == Environment.PRODUCTION.value:
        logger.info("Launching project in production environment")
        context = ProductionContext()
    else:
        logger.info("Launching project in development environment")
        context = DevelopmentContext()

    if args.host:
        context.server_host = args.host

    if args.port:
        context.server_port = args.port

    return context


def setup_logger(args: argparse.Namespace) -> None:
    if args.logging:
        logging_type = logger_type.LoggingType(args.logging)
        Logger.set_logger(logging_type)


def main():
    args = parse_args()

    setup_logger(args)
    app_context = get_application_context(args)

    app_launcher.launch(app_context)


if __name__ == "__main__":
    main()
