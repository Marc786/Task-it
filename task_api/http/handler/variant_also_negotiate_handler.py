from fastapi import Request, status
from fastapi.responses import JSONResponse

from task_api.config.logger.logger import Logger
from task_api.http.response.exception_response import ExceptionResponse

logger = Logger.get_logger()


async def variant_also_negotiate_handler(
        request: Request, exc: Exception
) -> JSONResponse:
    logger.info(
        f"An error occurred due to the specific server configuration ({request.method} {request.url.path})",
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_506_VARIANT_ALSO_NEGOTIATES,
        content=ExceptionResponse(
            detail=exc,
            request=request.url.path,
        ),
    )
