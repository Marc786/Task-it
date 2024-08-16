from fastapi import Request, status
from fastapi.responses import JSONResponse

from task_it.config.logger.logger import Logger
from task_it.core.commons.domain.exception.item_already_exists_exception import ItemAlreadyExistsException
from task_it.http.response.exception_response import ExceptionResponse

logger = Logger.get_logger()


async def item_already_exists_exception_handler(
    request: Request, exc: ItemAlreadyExistsException
) -> JSONResponse:
    logger.info(
        f"An error occurred due to a conflic with a specific item ({request.method} {request.url.path})",
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=ExceptionResponse(
            detail=str(exc),
            request=request.url.path,
        ).model_dump(),
    )
