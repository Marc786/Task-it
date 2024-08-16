from abc import ABC, abstractmethod

from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_id import TaskId
from task_it.core.task.domain.user.task_finder import TaskFinder


class TaskRepospitory(ABC, TaskFinder):
    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def find_by_id(self, task_id: TaskId) -> Task:
        pass

    @abstractmethod
    def find_all(self) -> list[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: TaskId) -> None:
        pass
    