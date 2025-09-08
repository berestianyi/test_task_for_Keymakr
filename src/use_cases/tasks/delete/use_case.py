from src.persistence.gateway.tasks import TaskGateway
from src.use_cases.abc import UseCaseABC
from .ports import TaskDeleteInput, TaskDeleteOutput


class TaskDeleteUseCase(UseCaseABC[TaskDeleteInput, TaskDeleteOutput]):

    def __init__(
            self,
            user_gateway: TaskGateway
    ):
        self._user_gateway = user_gateway

    async def execute(self, task_input: TaskDeleteInput) -> TaskDeleteOutput:

        is_deleted = await self._user_gateway.delete(task_input.id)

        return TaskDeleteOutput(is_deleted=is_deleted)
