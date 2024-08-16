from pydantic import BaseModel


class CreateAccountRequest(BaseModel):
    username: str
    password: str
    email: str
