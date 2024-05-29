from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.__user_repository.find_by_id(user_id)

    def get_users(self) -> list[User]:
        return self.__user_repository.find_all()

    def create_user(self, email: str, username: str) -> User:
        new_user = User(email, username)
        return self.__user_repository.save(new_user)
