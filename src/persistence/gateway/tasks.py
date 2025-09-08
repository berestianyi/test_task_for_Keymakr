import typing as t
from src.domain.entities.tasks import Task
from src.persistence.gateway.abc import GatewayABC
from src.persistence.mapper.tasks import TaskMapper
from src.persistence.repository.tasks import TaskRepository


class TaskGateway(GatewayABC[Task]):
    def __init__(self, repo: TaskRepository, mapper: TaskMapper):
        self._repo = repo
        self._mapper = mapper

    async def get_by_id(self, index: int) -> Task:
        dto = await self._repo.get_by_id(index)
        return self._mapper.to_domain(dto)


    async def list(self) -> t.List[Task]:
        dto_list = await self._repo.list()
        entity_list = [self._mapper.to_domain(entity) for entity in dto_list]
        return entity_list


    async def save(self, entity: Task) -> Task:
        dto = await self._repo.save(self._mapper.to_repository(entity))
        return self._mapper.to_domain(dto)


    async def update(self, entity: Task) -> Task:
        dto = await self._repo.update(self._mapper.to_repository(entity))
        return self._mapper.to_domain(dto)


    async def delete(self, index: int) -> bool:
        is_deleted = await self._repo.delete(index)
        return is_deleted