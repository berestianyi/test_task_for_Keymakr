from src.domain.entities.tasks import Task
from src.persistence.gateway.tasks import TaskGateway
from src.use_cases.abc import UseCaseABC
from .ports import TaskCreateInput, TaskCreateOutput


class TaskCreateUseCase(UseCaseABC[TaskCreateInput, TaskCreateOutput]):

    def __init__(
            self,
            user_gateway: TaskGateway
    ):
        self._user_gateway = user_gateway

    async def execute(self, task_input: TaskCreateInput) -> TaskCreateOutput:
        task = Task(
            title=task_input.title,
            description=task_input.description,
            completed=task_input.completed
        )

        saved_task = await self._user_gateway.save(task)

        return TaskCreateOutput(
            id=saved_task.id,
            title=saved_task.title,
            description=saved_task.description,
            completed=saved_task.completed
        )
