from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.config.db_helper import connection
from backend.domains.interface import AbstractInterface
from backend.models import HistoryWeather


class HistoryWeatherRepository(AbstractInterface):
    """Слой репозиторий"""

    model = HistoryWeather

    @connection
    async def find_top_five(self, session: AsyncSession):
        stmt = select(self.model).order_by(self.model.count_view.desc()).limit(5)
        result = await session.execute(stmt)
        instance = result.scalars().all()
        return instance

    @connection
    async def find_all(self, session: AsyncSession):
        stmt = select(self.model)
        result = await session.execute(stmt)
        instance = result.scalars().all()
        return instance

    @connection
    async def create_or_update(self, session: AsyncSession, city: str):
        stmt = select(self.model).filter_by(city=city)
        result = await session.execute(stmt)
        instance = result.scalar_one_or_none()

        if not instance:
            obj = self.model(city=city)
            session.add(obj)
            await session.commit()
            return obj

        instance.count_view += 1
        await session.commit()
        return instance
