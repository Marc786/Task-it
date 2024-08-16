from typing import Optional
from task_it.core.task.domain.task.exception.task_not_found_exception import TaskNotFoundException
from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_id import TaskId
from task_it.core.task.domain.task.task_repository import TaskRepospitory


class InMemoryTaskRepository(TaskRepospitory):
    __tasks: list[Task]
    
    def __init__(self):
        self.__tasks = []

    def find_all(self) -> list[Task]:
        return self.__tasks

    def find_by_id(self, task_id: TaskId) -> Optional[Task]:
        for task in self.__tasks:
            if task.get_id() == task_id:
                return task
        raise TaskNotFoundException()

    def save(self, task: Task) -> None:
        self.__tasks.append(task)

    def delete(self, task: Task) -> None:
        self.__tasks.remove(task)
