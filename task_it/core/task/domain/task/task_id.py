import uuid
from uuid import UUID


class TaskId:
    __value: UUID

    def __init__(self, value: str | None = None) -> None:
        self.__value = uuid.UUID(value) if value else uuid.uuid4()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TaskId):
            return False
        return self.__value == other.__value

    def __str__(self) -> str:
        return str(self.__value)
