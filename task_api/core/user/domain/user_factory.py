import re
from task_api.core.user.domain.email import Email
from task_api.core.user.domain.user import User
from task_api.core.user.domain.user_id import UserId
from task_api.core.user.domain.username import Username


class UserFactory:
    def create_user(self, email: Email, username: Username) -> User:
        self.__validate_email(email)
        user_id = UserId()
        return User(user_id, username, email)
    
    def __validate_email(self, email: Email) -> None:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not (re.match(pattern, email) is not None):
            raise ValueError('Invalid email format')
    