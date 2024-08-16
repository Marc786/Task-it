class UserId:
    __value: str

    def __init__(self, value: str):
        self.__value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserId):
            return False
        return self.__value == other.__value

    def __str__(self) -> str:
        return self.__value

    def __hash__(self) -> int:
        return hash(self.__value)
