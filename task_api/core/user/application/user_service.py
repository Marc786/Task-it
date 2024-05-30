from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_factory import UserFactory
from task_api.core.user.domain.user_repository import UserRepository


class UserService:
    __user_repository: UserRepository
    __user_factory: UserFactory
    
    def __init__(
        self,
        user_repository: UserRepository,
        user_factory: UserFactory,
    ):
        self.__user_repository = user_repository
        self.__user_factory = user_factory

    def get_user(self, username: str) -> User:
        return self.__user_repository.find_by_username(username)

    def get_users(self) -> list[User]:
        return self.__user_repository.find_all()

    def create_user(self, email: str, username: str) -> User:
        if self.__user_repository.find_by_username(username):
            raise ValueError(f'User with username {username} already exists')
        
        new_user = self.__user_factory.create_user(email, username)
        self.__user_repository.save(new_user)
        
        return new_user
