from task_it.core.account.domain.account_id import AccountId
from task_it.core.account.domain.email import Email
from task_it.core.account.domain.username import Username


class Account:
    __id: AccountId
    __username: Username
    __email: Email

    def __init__(self, id: AccountId, username: Username, email: Email):
        self.__id = id
        self.__username = username
        self.__email = email

    def get_id(self) -> AccountId:
        return self.__id

    def get_username(self) -> Username:
        return self.__username

    def get_email(self) -> Email:
        return self.__email

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return False
        return self.__id == other.__id
