from fastapi import APIRouter
from .weather.views import router as weather_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(weather_router)
