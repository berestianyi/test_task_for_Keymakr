from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, field_validator, model_validator


class Settings(BaseSettings):

    PROJECT_NAME: str = "test_task_for_Keymakr"
    DEBUG: bool = True

    REDIS_URL: str = "redis://:redispass@redis:6379/0"
    CELERY_BROKER_URL: str = "redis://:redispass@redis:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://:redispass@redis:6379/2"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )



settings = Settings()
