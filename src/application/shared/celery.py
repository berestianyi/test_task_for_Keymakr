from celery import Celery
from celery.schedules import crontab

from src.application.config import settings

celery = Celery(
    "app",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["src.application.shared.tasks"],
)

celery.conf.timezone = "UTC"
celery.conf.beat_schedule = {
    "fetch-users-every-1-min": {
        "task": "src.application.tasks.fetch_and_save_users_to_csv",
        "schedule": crontab(minute="*/1"),
        "args": (),
    }
}