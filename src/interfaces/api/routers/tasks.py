from fastapi import APIRouter, Depends, HTTPException, status, Response

from src.application.shared.dependency_injection.use_case import get_task_create_use_case, get_task_list_use_case, \
    get_task_update_use_case, get_task_delete_use_case
from src.interfaces.api.schemas.tasks import TaskCreate, TaskOutput, TaskUpdate
from src.use_cases.tasks.create.ports import TaskCreateInput
from src.use_cases.tasks.create.use_case import TaskCreateUseCase
from src.use_cases.tasks.delete.ports import TaskDeleteInput
from src.use_cases.tasks.delete.use_case import TaskDeleteUseCase
from src.use_cases.tasks.get_list.use_case import TaskGetListUseCase
from src.use_cases.tasks.update.ports import TaskUpdateInput
from src.use_cases.tasks.update.use_case import TaskUpdateUseCase

task_router = APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.post("", response_model=TaskOutput, status_code=201)
async def create(
        data: TaskCreate,
        uc: TaskCreateUseCase = Depends(get_task_create_use_case),
) -> TaskOutput:
    try:
        output = await uc.execute(
            TaskCreateInput(
                title=data.title,
                description=data.description,
                completed=data.completed
            )
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    return TaskOutput(
        id=output.id,
        title=output.title,
        description=output.description,
        completed=output.completed
    )


@task_router.get("", response_model=list[TaskOutput])
async def list_tasks(
        uc: TaskGetListUseCase = Depends(get_task_list_use_case),
) -> list[TaskOutput]:
    try:
        result = await uc.execute()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    return [
        TaskOutput(
            id=output.id,
            title=output.title,
            description=output.description,
            completed=output.completed
        )
        for output in result]


@task_router.put("/{task_id}", response_model=TaskOutput, status_code=201)
async def update(
        task_id: int,
        data: TaskUpdate,
        uc: TaskUpdateUseCase = Depends(get_task_update_use_case),
):
    try:
        output = await uc.execute(
            TaskUpdateInput(
                id=task_id,
                title=data.title,
                description=data.description,
                completed=data.completed
            )
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    return TaskOutput(
        id=output.id,
        title=output.title,
        description=output.description,
        completed=output.completed
    )


@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        task_id: int,
        uc: TaskDeleteUseCase = Depends(get_task_delete_use_case),
):
    try:
        is_deleted = await uc.execute(TaskDeleteInput(id=task_id))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)