from fastapi import APIRouter
from app.utils import HttpResponseBuilder
from app.config import AppConfig

routes = APIRouter()
config = AppConfig.config

