from fastapi import APIRouter, BackgroundTasks

from backend.api.v1.weather.schemas import WeatherResponse
from backend.domains.service import history_weather
from backend.api.v1.weather.utils import get_weather

router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)


@router.get("/history")
async def get_history():
    """
    Получить все записи
    """
    return await history_weather.find_all()


@router.get("/top/five")
async def top_five():
    """
    Получить только 5 городов у который наибольшее количество запросов
    :return:
    """
    result = await history_weather.find_top_five()
    return [await get_weather(city=_.city) for _ in result]


@router.get("/weather/", response_model=WeatherResponse)
async def get_geo_data(city: str, bg: BackgroundTasks):
    """Получить погоду по городу и сохранить данные в БД"""
    result = await get_weather(city=city)
    bg.add_task(history_weather.create_or_update, city)
    return result
