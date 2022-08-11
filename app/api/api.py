from datetime import datetime
from typing import Optional, Any

from fastapi import APIRouter

from app.core.settings import settings

api_router = APIRouter()


@api_router.get("/")
def root():
    return {}


@api_router.get("/ping")
def ping(q: Optional[str] = None) -> Any:
    """
    Responds to health check api call. Right now it just returns
    """
    return {"service": settings.PROJECT_NAME, "query": q, "t": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
