from task_it.core.task.domain.task.description import Description
from task_it.core.task.domain.task.status import Status
from task_it.core.task.domain.task.task_id import TaskId
from task_it.core.task.domain.task.title import Title


class Task:
    __id: TaskId
    __title: Title
    __description: Description
    __status: Status
    
    def __init__(self, id: TaskId, title: Title, description: Description, status: Status):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__status = status
    
    def get_id(self) -> TaskId:
        return self.__id
    
    def get_title(self) -> Title:
        return self.__title
    
    def get_description(self) -> Description:
        return self.__description
    
    def get_status(self) -> Status:
        return self.__status
    
    def mark_as_done(self) -> None:
        self.__status = Status.DONE
