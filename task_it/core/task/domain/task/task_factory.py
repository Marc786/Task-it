from task_it.core.task.domain.task.status import Status
from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_id import TaskId


class TaskFactory:
    def create(self, task_id: TaskId, title: str, description: str) -> Task:
        return Task(task_id, title, description, Status.TODO)
    