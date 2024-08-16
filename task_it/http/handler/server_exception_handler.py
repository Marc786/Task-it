from fastapi import Request, status
from fastapi.responses import JSONResponse

from task_it.config.logger.logger import Logger
from task_it.http.response.exception_response import ExceptionResponse

logger = Logger.get_logger()


async def server_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(
        f"An unexpected exception occurred ({request.method} {request.url.path})",
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ExceptionResponse(
            detail=str(exc),
            request=request.url.path,
        ).model_dump(),
    )
