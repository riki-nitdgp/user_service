from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.utils import HttpResponseBuilder
from .exceptions import InternalServerError, BadRequestException, NotFoundException, UnAuthorizedException, \
    ForbiddenException
from starlette import status
import traceback


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.detail, status_code=exc.status_code)


async def internal_service_error_handler(_: Request, exc: InternalServerError) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.error, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def bad_request_exception_handler(_: Request, exc: BadRequestException) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.error, status_code=status.HTTP_400_BAD_REQUEST)


async def not_found_exception_handler(_: Request, exc: NotFoundException) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.error, status_code=status.HTTP_204_NO_CONTENT)


async def unauthorized_exception_handler(_: Request, exc: UnAuthorizedException) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.error, status_code=status.HTTP_401_UNAUTHORIZED)


async def forbidden_exception_handler(_: Request, exc: ForbiddenException) -> JSONResponse:
    return await HttpResponseBuilder.build_error_response(exc.error, status_code=status.HTTP_403_FORBIDDEN)


async def debug_exception_handler(_: Request, exc: Exception):
    error = "".join(traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__))
    # _.app.logger.error(error)
    return await HttpResponseBuilder.build_error_response(error, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
