class Title:
    def __init__(self, value: str):
        self.value = value
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Title):
            return False
        return self.value == other.value
    
    def __str__(self) -> str:
        return self.value
    