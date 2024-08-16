from task_it.core.task.domain.user.user import User
from task_it.core.task.domain.user.user_id import UserId


class UserFactory:
    def create(self) -> User:
        user_id = UserId()
        tasks = []
        return User(user_id, tasks)
