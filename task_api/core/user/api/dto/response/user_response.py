from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
