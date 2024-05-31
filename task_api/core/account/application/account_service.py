from task_api.core.account.domain.account import Account
from task_api.core.account.domain.account_factory import AccountFactory
from task_api.core.account.domain.account_repository import AccountRepository


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

    def get_account(self, username: str) -> Account:
        return self.__account_repository.find_by_username(username)

    def get_account(self) -> list[Account]:
        return self.__account_repository.find_all()

    def create_account(self, email: str, username: str) -> Account:
        if self.__account_repository.find_by_username(username):
            raise ValueError(f"User with username {username} already exists")

        new_account = self.__account_factory.create_account(email, username)
        self.__account_repository.save(new_account)

        return new_account
