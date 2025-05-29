"""Схемы или DTO"""

from datetime import datetime

from pydantic import BaseModel


class CityForm(BaseModel):
    city: str


class WeatherResponse(CityForm):
    time: datetime
    interval: int
    temperature_2m: float
    precipitation: float
    rain: float
    surface_pressure: float
    wind_speed_10m: float
    wind_direction_10m: float
    wind_gusts_10m: float
