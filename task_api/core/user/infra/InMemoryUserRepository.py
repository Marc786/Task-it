from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_id import UserId
from task_api.core.user.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    __users: list[User]

    def __init__(self):
        self.__users = []

    def find_by_id(self, user_id: UserId) -> User:
        return next((user for user in self.__users if user.get_id() == user_id), None)

    def find_all(self) -> list[User]:
        return self.__users

    def save(self, user: User) -> User:
        self.__users = [u if u.get_id() != user.get_id() else user for u in self.__users]
        return user
    