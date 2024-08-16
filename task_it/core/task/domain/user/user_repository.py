from abc import ABC, abstractmethod

from task_it.core.task.domain.user.user import User
from task_it.core.task.domain.user.user_id import UserId


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def find_all(self) -> list[User]:
        pass

    @abstractmethod
    def delete(self, user_id: UserId) -> None:
        pass
