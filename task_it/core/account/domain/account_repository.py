from abc import ABC, abstractmethod

from task_it.core.account.domain.account import Account
from task_it.core.account.domain.account_id import AccountId


class AccountRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: AccountId) -> Account:
        pass

    @abstractmethod
    def find_all(self) -> list[Account]:
        pass

    @abstractmethod
    def save(self, account: Account) -> Account:
        pass
