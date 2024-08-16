from fastapi import Request, status
from fastapi.responses import JSONResponse

from task_it.config.logger.logger import Logger
from task_it.core.commons.domain.exception.configuration_exception import ConfigurationException
from task_it.http.response.exception_response import ExceptionResponse

logger = Logger.get_logger()


async def server_config_exception_handler(
    request: Request, exc: ConfigurationException
) -> JSONResponse:
    logger.info(
        f"An error occurred due to the specific server configuration ({request.method} {request.url.path})",
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_506_VARIANT_ALSO_NEGOTIATES,
        content=ExceptionResponse(
            detail=str(exc),
            request=request.url.path,
        ).model_dump(),
    )
