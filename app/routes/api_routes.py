from fastapi import APIRouter
from app.routes.handlers import (
    health,
    user_handler
)

router = APIRouter()

router.include_router(health.routes, tags=["health-check"], prefix='/health')
router.include_router(user_handler.routes, tags=["health-check"], prefix='/user')
