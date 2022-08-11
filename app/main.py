from fastapi import FastAPI

from app.api.api import api_router
from app.core.settings import settings, Settings


def get_application(app_config: Settings) -> FastAPI:
    application = FastAPI(title=app_config.PROJECT_NAME)

    application.include_router(api_router)
    return application


app = get_application(settings)
