from task_api.core.user.domain.email import Email
from task_api.core.user.domain.user_id import UserId
from task_api.core.user.domain.username import Username


class User:
    __id: UserId
    __username: Username
    __email: Email

    def __init__(self, id: UserId, username: Username, email: Email):
        self.__id = id
        self.__username = username
        self.__email = email

    def get_id(self) -> UserId:
        return self.__id

    def get_username(self) -> Username:
        return self.__username

    def get_email(self) -> Email:
        return self.__email

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.__id == other.__id
