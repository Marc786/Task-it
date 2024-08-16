from abc import ABC, abstractmethod

from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_id import TaskId


class TaskFinder(ABC):
    @abstractmethod
    def find_by_id(self, task_id: TaskId) -> Task:
        pass
