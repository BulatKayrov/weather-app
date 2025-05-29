"""
Вспомогательные утилиты для работы с API
п.с. Сделал выбор в пользу aiohttp
"""

import httpx
from geopy.geocoders import Nominatim

import aiohttp


def format_city(city: str) -> tuple[float, float]:
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(city)

    return location.latitude, location.longitude


async def get_weather(city: str):
    latitude, longitude = format_city(city=city)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&wind_speed_unit=ms"

    async with aiohttp.ClientSession() as session:
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
