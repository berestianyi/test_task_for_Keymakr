from pathlib import Path

from src.application.shared.celery import celery
from src.application.config import settings
from src.persistence.gateway.CSV.users import UserCSVGateway
from src.use_cases.ml.train.ports import TrainModelInput
from src.use_cases.ml.train.use_case import TrainModelUseCase
from src.use_cases.users.save.ports import SaveUserToCSVInput
from src.use_cases.users.save.use_case import SaveUserToCSVUseCase

@celery.task(name="src.application.tasks.fetch_and_save_users_to_csv")
def fetch_and_save_users_to_csv(url: str | None = None) -> Path:
    uc = SaveUserToCSVUseCase(user_gateway=UserCSVGateway())
    inp = SaveUserToCSVInput(url=url or settings.USERS_API_URL)
    out = uc.execute(inp)
    return out.path

@celery.task(name="src.application.tasks.train_model_task")
def train_model_task(csv_path: str | None = None, out_path: str | None = None) -> str:
    out =  TrainModelUseCase().execute(TrainModelInput(csv_path=csv_path, out_path=out_path))
    return str(out.path)