from fastapi import APIRouter
from app.utils import HttpResponseBuilder
from app.config import AppConfig

routes = APIRouter()
config = AppConfig.config


@routes.get('')
async def health_check():
    data = {"message": "{service_name} Service is Up Now !!!!".format(service_name=config.get("SERVICE_NAME"))}
    return await HttpResponseBuilder.build_success_response(data)
