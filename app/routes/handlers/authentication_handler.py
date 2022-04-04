from fastapi import APIRouter, Request
from app.utils import HttpResponseBuilder
from app.service.auth import AuthorizationManager
from app.config import AppConfig
from app.data_validator import DataValidator

routes = APIRouter()
config = AppConfig.config


@routes.post("/authenticate")
async def authenticate_user(_request: Request):
    headers = _request.headers
    authorization_token = headers.get("x-authorization-token")
    DataValidator.validate_mandatory_params(authorization_token=authorization_token)
    authorized_user = await AuthorizationManager.authorized_user(authorization_token)
    return await HttpResponseBuilder.build_success_response(authorized_user)
