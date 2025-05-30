from backend.domains.interface import AbstractInterface
from backend.domains.repository import HistoryWeatherRepository


class HistoryWeatherService:
    """Сервисный слой"""

    def __init__(self, repository: AbstractInterface):
        self.repository = repository

    async def find_top_five(self):
        return await self.repository.find_top_five()

    async def create_or_update(self, city: str):
        return await self.repository.create_or_update(city=city)

    async def find_all(self):
        return await self.repository.find_all()


history_weather = HistoryWeatherService(repository=HistoryWeatherRepository())
