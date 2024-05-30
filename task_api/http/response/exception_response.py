from pydantic import BaseModel


class ExceptionResponse(BaseModel):
    request: str
    detail: str
