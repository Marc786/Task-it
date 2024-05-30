from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_id import UserId
from task_api.core.user.domain.user_repository import UserRepository
from task_api.core.user.domain.username import Username


class InMemoryUserRepository(UserRepository):
    __users: list[User]

    def __init__(self):
        self.__users = []

    def find_by_username(self, username: Username) -> User:
        return next((user for user in self.__users if user.get_username() == username), None)

    def find_all(self) -> list[User]:
        return self.__users

    def save(self, user: User) -> None:
        if self.find_by_username(user.get_username()):
            self.__users.remove(user)
        self.__users.append(user)
