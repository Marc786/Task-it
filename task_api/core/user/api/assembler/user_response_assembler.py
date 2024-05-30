from task_api.core.user.api.dto.response.user_response import UserResponse
from task_api.core.user.domain.user import User


class UserResponseAssembler:
    def user_to_response(self, user: User):
        return UserResponse(
            id=str(user.get_id()),
            username=str(user.get_username()),
            email=str(user.get_email()),
        )

    def users_to_response(self, users: list[User]):
        return [self.user_to_response(user) for user in users]
