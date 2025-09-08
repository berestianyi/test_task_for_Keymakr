from fastapi import Depends

from .persistence import get_task_gateway
from src.persistence.gateway.tasks import TaskGateway
from src.use_cases.tasks.create.use_case import TaskCreateUseCase
from src.use_cases.tasks.delete.use_case import TaskDeleteUseCase
from src.use_cases.tasks.get_list.use_case import TaskGetListUseCase
from src.use_cases.tasks.update.use_case import TaskUpdateUseCase




def get_task_create_use_case(
        gateway: TaskGateway = Depends(get_task_gateway),
):
    return TaskCreateUseCase(gateway)


def get_task_delete_use_case(
        gateway: TaskGateway = Depends(get_task_gateway),
):
    return TaskDeleteUseCase(gateway)


def get_task_update_use_case(
        gateway: TaskGateway = Depends(get_task_gateway),
):
    return TaskUpdateUseCase(gateway)


def get_task_list_use_case(
        gateway: TaskGateway = Depends(get_task_gateway),
):
    return TaskGetListUseCase(gateway)
