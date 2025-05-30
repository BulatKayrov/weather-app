"""
Вспомогательные утилиты для работы с API
п.с. Сделал выбор в пользу aiohttp
"""

import httpx
from aiohttp import ClientTimeout
from geopy.adapters import AioHTTPAdapter
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

import aiohttp


async def format_city(city: str) -> tuple[float, float]:
    async with Nominatim(
        user_agent="app",
        adapter_factory=AioHTTPAdapter,
        timeout=3,
    ) as geolocator:
        location = await geolocator.geocode(city)

    return location.latitude, location.longitude


async def get_weather(city: str):
    try:
        latitude, longitude = await format_city(city=city)
    except GeocoderTimedOut:
        latitude, longitude = await format_city(city=city)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&wind_speed_unit=ms"

    async with aiohttp.ClientSession(timeout=ClientTimeout(2)) as session:
        async with session.get(url) as response:
            response = await response.json()
            data = response.get("current")
            data["city"] = city
            return data

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url)
    #     data = response.json().get("current")
    #     data["city"] = city
    #     return data
