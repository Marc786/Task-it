import re

from task_it.core.account.domain.account import Account
from task_it.core.account.domain.account_id import AccountId
from task_it.core.account.domain.email import Email
from task_it.core.account.domain.username import Username


class AccountFactory:
    def create_account(self, email: Email, username: Username) -> Account:
        self.__validate_email(email)
        account_id = AccountId()
        return Account(account_id, username, email)

    def __validate_email(self, email: Email) -> None:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not (re.match(pattern, email) is not None):
            raise ValueError("Invalid email format")
