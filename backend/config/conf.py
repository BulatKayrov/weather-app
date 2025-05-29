from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """Настройки для всего проекта"""

    @property
    def dev_db_url(self):
        db_path = BASE_DIR / "database.db"
        return f"sqlite+aiosqlite:///{db_path.as_posix()}"


settings = Settings()
