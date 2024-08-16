from pydantic import BaseModel


class AccountResponse(BaseModel):
    id: str
    username: str
    email: str
