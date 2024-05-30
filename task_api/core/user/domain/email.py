class Email:
    __email: str
    
    def __init__(self, email: str):
        self.__email = email
    
    def __str__(self) -> str:
        return self.__email

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Email):
            return False
        return self.__email == other.__email
