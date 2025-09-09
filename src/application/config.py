from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, field_validator, model_validator, AnyUrl


class Settings(BaseSettings):

    PROJECT_NAME: str = "test_task_for_Keymakr"
    DEBUG: bool = True

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_URL: str = "redis://redis:6379/0"
    CELERY_BROKER_URL: str = "redis://redis:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/2"

    USERS_API_URL: str = "https://jsonplaceholder.typicode.com/users"
    USERS_CSV_PATH: Path = Path("/app/data/csv")

    TASKS_CSV_PATH: Path = Path("/app/data/ml/tasks.csv")
    MODEL_PATH: Path = Path("/app/data/models/priority_model.joblib")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )



settings = Settings()

settings.MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)