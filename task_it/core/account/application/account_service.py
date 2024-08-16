from task_it.core.account.domain.account import Account
from task_it.core.account.domain.account_factory import AccountFactory
from task_it.core.account.domain.account_repository import AccountRepository
from task_it.core.account.domain.email import Email
from task_it.core.account.domain.username import Username


class AccountService:
    __account_repository: AccountRepository
    __account_factory: AccountFactory

    def __init__(
        self,
        account_repository: AccountRepository,
        account_factory: AccountFactory,
    ):
        self.__account_repository = account_repository
        self.__account_factory = account_factory

    def get_account(self, username: Username) -> Account:
        return self.__account_repository.find_by_username(username)

    def get_accounts(self) -> list[Account]:
        return self.__account_repository.find_all()

    def create_account(self, email: Email, username: Username) -> Account:
        if self.__account_repository.find_by_username(username):
            raise ValueError(f"User with username {username} already exists")

        new_account = self.__account_factory.create_account(email, username)
        self.__account_repository.save(new_account)

        return new_account
