from abc import ABC, abstractmethod

from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_id import UserId


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def find_all(self) -> list[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
