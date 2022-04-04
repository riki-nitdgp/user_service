from fastapi import APIRouter, Request
from app.utils import HttpResponseBuilder
from app.data_validator import DataValidator
from app.config import AppConfig
from app.service import UserManager


routes = APIRouter()
config = AppConfig.config


@routes.post("/sign-up")
async def user_signup(_request: Request):
    payload = await _request.json()
    email = payload.get("email")
    phone_number = payload.get("phone_number")
    password = payload.get("password")

    DataValidator.validate_email(email)
    DataValidator.validate_phone_number(phone_number)
    DataValidator.validate_password(password)

    result = await UserManager.sign_up(email, phone_number, password)
    return await HttpResponseBuilder.build_success_response(result)


@routes.post("/login")
async def login(_request: Request):
    payload = await _request.json()
    email = payload.get("email")
    password = payload.get("password")
    DataValidator.validate_email(email)
    DataValidator.validate_password(password)
    result = await UserManager.login(email, password)
    return await HttpResponseBuilder.build_success_response(result)