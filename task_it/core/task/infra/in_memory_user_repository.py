from typing import Optional
from task_it.core.task.domain.user.exception.user_not_found_exception import UserNotFoundException
from task_it.core.task.domain.user.user import User
from task_it.core.task.domain.user.user_id import UserId
from task_it.core.task.domain.user.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    __users: list[User]
    
    def __init__(self):
        self.__users = []

    def find_by_id(self, user_id: UserId) -> Optional[User]:
        for user in self.__users:
            if user.get_id() == user_id:
                return user
        raise UserNotFoundException()

    def save(self, user: User) -> None:
        self.__users.append(user)
