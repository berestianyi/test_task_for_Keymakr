import typing as t

from src.persistence.gateway.tasks import TaskGateway
from src.use_cases.abc import NoInputUseCaseABC
from .ports import TaskGetListOutput


class TaskGetListUseCase(NoInputUseCaseABC[TaskGetListOutput]):

    def __init__(
            self,
            user_gateway: TaskGateway
    ):
        self._user_gateway = user_gateway

    async def execute(self) -> t.List[TaskGetListOutput]:

        saved_tasks = await self._user_gateway.list()

        return [TaskGetListOutput(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=task.completed
        ) for task in saved_tasks]
