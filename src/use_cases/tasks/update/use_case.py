from src.domain.entities.tasks import Task
from src.persistence.gateway.tasks import TaskGateway
from src.use_cases.abc import UseCaseABC
from .ports import TaskUpdateOutput, TaskUpdateInput


class TaskUpdateUseCase(UseCaseABC[TaskUpdateInput, TaskUpdateOutput]):

    def __init__(
            self,
            user_gateway: TaskGateway
    ):
        self._user_gateway = user_gateway

    async def execute(self, task_input: TaskUpdateInput) -> TaskUpdateOutput:
        task = Task(
            id=task_input.id,
            title=task_input.title,
            description=task_input.description,
            completed=task_input.completed
        )

        saved_task = await self._user_gateway.update(task)

        return TaskUpdateOutput(
            id=saved_task.id,
            title=saved_task.title,
            description=saved_task.description,
            completed=saved_task.completed
        )
