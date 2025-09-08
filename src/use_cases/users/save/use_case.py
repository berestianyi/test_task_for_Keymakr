from src.application.config import settings
from src.domain.entities.users import User
from src.interfaces.api.fetch.users import fetch_users
from src.persistence.gateway.CSV.users import UserCSVGateway
from src.use_cases.abc import UseCaseABC
from .ports import SaveUserToCSVInput, SaveUserToCSVOutput


class SaveUserToCSVUseCase(UseCaseABC[SaveUserToCSVInput, SaveUserToCSVOutput]):

    def __init__(
            self,
            user_gateway: UserCSVGateway
    ):
        self._user_gateway = user_gateway

    def execute(self, user_input: SaveUserToCSVInput) -> SaveUserToCSVOutput:
        users_json = fetch_users(user_input.url)
        users = [
            User(
                id=user.get("id"),
                name=user.get("name"),
                email=user.get("email")
            )
            for user in users_json
        ]

        path = self._user_gateway.save(entities=users, path= settings.USERS_CSV_PATH)

        return SaveUserToCSVOutput(path=path)
