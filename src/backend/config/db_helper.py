from contextlib import asynccontextmanager
from functools import wraps

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from backend.config.conf import settings

engine = create_async_engine(url=settings.dev_db_url)
Session = async_sessionmaker(
    bind=engine, expire_on_commit=False, autocommit=False, autoflush=False
)


@asynccontextmanager
async def session_scope():
    """Если нужно использовать в зависимости"""
    async with Session() as session:
        yield session


def connection(func):
    """декоратор для передачи сессии в слой репозиторий"""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with Session() as session:
            try:
                result = await func(session=session, *args, **kwargs)
                return result
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    return wrapper
