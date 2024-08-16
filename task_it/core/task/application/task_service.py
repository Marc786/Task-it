from task_it.core.task.domain.task.task import Task
from task_it.core.task.domain.task.task_repository import TaskRepospitory
from task_it.core.task.domain.user.exception.user_not_found_exception import UserNotFoundException
from task_it.core.task.domain.user.user import User
from task_it.core.task.domain.user.user_factory import UserFactory
from task_it.core.task.domain.user.user_id import UserId
from task_it.core.task.domain.user.user_repository import UserRepository


class TaskService:
    __task_repository: TaskRepospitory
    __user_repository: UserRepository
    __user_factory: UserFactory

    def __init__(self, task_repository: TaskRepospitory, user_repository: UserRepository, user_factory: UserFactory):
        self.__task_repository = task_repository
        self.__user_repository = user_repository
        self.__user_factory = user_factory

    def create_task(self, task: Task):
        self.__task_repository.save(task)

    def get_task(self, task_id: str) -> Task:
        return self.__task_repository.find_by_id(task_id)

    def get_tasks(self) -> list[Task]:
        return self.__task_repository.find_all()
    
    def delete_task(self, task_id: str):
        self.__task_repository.delete(task_id)

    def retrieve_user(self, user_id: UserId) -> User:
        try:
            return self.__user_repository.find_by_id(user_id)
        except UserNotFoundException:
            return self.__user_factory.create()
