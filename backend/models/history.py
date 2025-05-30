from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class HistoryWeather(Base):
    """История городов"""

    __tablename__ = "history_weather"

    city: Mapped[str] = mapped_column(unique=True)
    count_view: Mapped[int] = mapped_column(default=1)

    def __repr__(self):
        return f"<HistoryWeather: {self.city}>"
