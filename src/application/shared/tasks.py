from pathlib import Path

from src.application.shared.celery import celery
from src.application.config import settings
from src.persistence.gateway.CSV.users import UserCSVGateway
from src.use_cases.users.save.ports import SaveUserToCSVInput
from src.use_cases.users.save.use_case import SaveUserToCSVUseCase

@celery.task(name="src.application.tasks.fetch_and_save_users_to_csv")
def fetch_and_save_users_to_csv(url: str | None = None) -> Path:
    uc = SaveUserToCSVUseCase(user_gateway=UserCSVGateway())
    inp = SaveUserToCSVInput(url=url or settings.USERS_API_URL)
    out = uc.execute(inp)
    return out.path
