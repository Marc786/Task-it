from task_api.config.context.application_context import ApplicationContext
from task_api.config.context.environment import Environment
from task_api.config.logger.logger import Logger
from task_api.core.user.api.config.user_dependency_factory import (
    create_in_memory_user_repository,
)
from task_api.core.user.domain.user_repository import UserRepository

logger = Logger.get_logger()


class ProductionContext(ApplicationContext):
    ENV = Environment.PRODUCTION
    HOST_IP = "10.0.0.1"
    PORT = 8080

    def __init__(self):
        super().__init__(self.ENV, self.HOST_IP, self.PORT)

    def initialize_dependencies(self):
        super().initialize_dependencies()

    def create_user_repository(self) -> UserRepository:
        return create_in_memory_user_repository()
