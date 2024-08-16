class Username:
    __username: str

    def __init__(self, username: str):
        self.__username = username

    def __str__(self) -> str:
        return self.__username

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Username):
            return False
        return self.__username == other.__username
