from fastapi import Request, status
from fastapi.responses import JSONResponse

from task_api.config.logger.logger import Logger
from task_api.exception.invalid_input_exception import InvalidInputException
from task_api.http.response.exception_response import ExceptionResponse

logger = Logger.get_logger()


async def invalid_input_exception_handler(
    request: Request, exc: InvalidInputException
) -> JSONResponse:
    logger.info(
        f"An error occurred due to invalid data in the request ({request.method} {request.url.path})",
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ExceptionResponse(
            detail=str(exc),
            request=request.url.path,
        ).model_dump(),
    )
