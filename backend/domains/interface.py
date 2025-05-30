from abc import ABC, abstractmethod


class AbstractInterface(ABC):
    """Базовый интерфейс"""

    model = None

    @abstractmethod
    async def find_top_five(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create_or_update(self, *args, **kwargs):
        pass

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        pass
