from src.persistence.gateway.tasks import TaskGateway
from src.persistence.mapper.tasks import TaskMapper
from src.persistence.repository.tasks import TaskRepository


def get_task_gateway():
    return TaskGateway(
        repo=TaskRepository(),
        mapper=TaskMapper()
    )