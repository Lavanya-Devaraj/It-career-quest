from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolves to Backend/.env regardless of the current working directory.
_ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    APP_NAME: str = "IT Career Quest API"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=str(_ENV_FILE),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
