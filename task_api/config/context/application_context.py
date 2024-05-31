from abc import ABC, abstractmethod

from task_api.config.context.environment import Environment
from task_api.config.logger.logger import Logger
from task_api.config.service_locator import ServiceLocator
from task_api.core.account.domain.account_repository import AccountRepository

logger = Logger.get_logger()


class ApplicationContext(ABC):

    def __init__(self, env: Environment, server_host: str, server_port: int):
        self.env = env
        self.server_host = server_host
        self.server_port = server_port

    @abstractmethod
    def initialize_dependencies(self):
        logger.info("Initializing dependencies...")

        dependencies = [
            (AccountRepository, self.create_user_repository()),
        ]

        ServiceLocator.clear()

        for dependency in dependencies:
            dependency_type = dependency[0]
            dependency_instance = dependency[1]
            ServiceLocator.register_dependency(dependency_type, dependency_instance)

        logger.info("Application's dependencies initialized successfully")

    @abstractmethod
    def create_user_repository(self) -> AccountRepository:
        pass
