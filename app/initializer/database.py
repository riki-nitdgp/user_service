from app.config import AppConfig
from tortoise import Tortoise
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


class InitializeDBManager:
    db_config = AppConfig.config["DATABASE"]

    @classmethod
    def init_db(cls, app):
        models = []
        register_tortoise(
            app,
            db_url="sqlite://db.sqlite3",
            modules={"models": ["app.models"]},
            generate_schemas=True,
            add_exception_handlers=True,
        )
