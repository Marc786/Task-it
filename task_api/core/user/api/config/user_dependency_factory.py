from task_api.config.service_locator import ServiceLocator
from task_api.core.user.application.user_service import UserService
from task_api.core.user.domain.user_factory import UserFactory
from task_api.core.user.domain.user_repository import UserRepository
from task_api.core.user.infra.InMemoryUserRepository import InMemoryUserRepository


def create_user_service():
    user_repository = ServiceLocator().get_dependency(UserRepository)

    user_service = UserService(user_repository, UserFactory())
    return user_service


def create_in_memory_user_repository():
    return InMemoryUserRepository()
