from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):
    """Настройки для всего проекта"""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        # env_nested_delimiter='__',    # Разделитель
        env_file=f"{BASE_DIR}/.env",
        env_file_encoding="utf-8",
    )

    HOST: str
    PORT: int

    @property
    def dev_db_url(self):
        db_path = BASE_DIR / "database.db"
        return f"sqlite+aiosqlite:///{db_path.as_posix()}"


settings = Settings()
