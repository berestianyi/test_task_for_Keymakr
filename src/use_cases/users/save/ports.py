from src.application.config import settings
from src.use_cases.abc import Input, SuccessfulOutput



class SaveUserToCSVInput(Input):
    url: str = settings.USERS_API_URL



class SaveUserToCSVOutput(SuccessfulOutput):
    path: str


