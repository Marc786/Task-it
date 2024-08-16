from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_id import TaskId
from task_it.core.task.domain.user.task_finder import TaskFinder
from task_it.core.task.domain.user.user_id import UserId


class User:
    __id: UserId
    __tasks: list[TaskId]

    def __init__(self, id: UserId, tasks):
        self.__id = id
        self.tasks = tasks

    def get_id(self) -> UserId:
        return self.__id

    def get_tasks(self) -> list[TaskId]:
        return self.__tasks

    def add_task(self, task: Task) -> None:
        self.__tasks.append(task.get_id())

    def remove_task(self, task: Task) -> None:
        self.__tasks.remove(task.get_id())

    def mark_task_as_done(self, task_id: TaskId, task_finder: TaskFinder) -> None:
        task = task_finder.find_by_id(task_id)
        task.mark_as_done()
        
        