
from task_api.config.context.application_context import ApplicationContext
from task_api.config.context.environment import Environment
from task_api.config.logger.logger import Logger


logger = Logger.get_logger()


class ProductionContext(ApplicationContext):
    HOST_IP = "10.0.0.1"
    PORT = 8080
    ENV = Environment.PRODUCTION

    def __init__(self):
        super().__init__(self.ENV, self.HOST_IP, self.PORT)

    def initialize_dependencies(self):
        super().initialize_dependencies()

    def create_something(self):
        return "something"
    