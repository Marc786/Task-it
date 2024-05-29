from task_api.core.user.domain.user_id import UserId


class User:
    def __init__(self, id: UserId, username: str, email: str):
        self.__id = id
        self.__username = username
        self.__email = email

    def get_id(self) -> UserId:
        return self.__id

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.__id == other.__id
