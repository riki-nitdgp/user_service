from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from app.routes.api_routes import router as api_router
from fastapi import Request
from app.config import AppConfig
from app.initializer import InitializeDBManager
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app.utils import HttpResponseBuilder
from app.exception import (
    UnAuthorizedException,
    NotFoundException,
    ForbiddenException,
    BadRequestException,
    InternalServerError,
    http_error_handler,
    debug_exception_handler,
    internal_service_error_handler,
    bad_request_exception_handler,
    not_found_exception_handler,
    unauthorized_exception_handler,
    forbidden_exception_handler
)


def create_application() -> FastAPI:
    config = AppConfig.config
    application = FastAPI(title=config.get("SERVICE_NAME"), debug=config.get("DEBUG"))
    application.include_router(api_router, prefix=config.get("API_PREFIX"))
    add_exception_handler(application)
    InitializeDBManager.init_db(application)
    if config.get("ENABLE_OPEN_TELEMETRY"):
        FastAPIInstrumentor().instrument();
    return application


def add_exception_handler(application: FastAPI):
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(Exception, debug_exception_handler)
    application.add_exception_handler(UnAuthorizedException, unauthorized_exception_handler)
    application.add_exception_handler(BadRequestException, bad_request_exception_handler)
    application.add_exception_handler(ForbiddenException, forbidden_exception_handler)
    application.add_exception_handler(NotFoundException, not_found_exception_handler)
    application.add_exception_handler(InternalServerError, internal_service_error_handler)


app = create_application()
