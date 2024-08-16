from typing import Optional
from task_it.core.account.domain.account import Account
from task_it.core.account.domain.account_repository import AccountRepository
from task_it.core.account.domain.username import Username


class InMemoryAccountRepository(AccountRepository):
    __accounts: list[Account]

    def __init__(self):
        self.__accounts = []

    def find_by_username(self, username: Username) -> Optional[Account]:
        return next(
            (user for user in self.__accounts if user.get_username() == username), None
        )

    def find_all(self) -> list[Account]:
        return self.__accounts

    def save(self, account: Account) -> None:
        if self.find_by_username(account.get_username()):
            self.__accounts.remove(account)
        self.__accounts.append(account)
