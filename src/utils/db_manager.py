from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.utils.env_constants import DATABASE_URI, MODELS_PATH

MIGRATION_CONFIG = {
    "connections": {"default": DATABASE_URI},
    "apps": {
        "models": {
            "models": [MODELS_PATH, "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URI,
        modules={"models": [MODELS_PATH]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
