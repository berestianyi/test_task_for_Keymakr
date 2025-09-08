from dataclasses import dataclass

from pydantic import BaseModel
import redis.asyncio as Redis

from .abc import RepositoryABC
from src.application.config import settings


class TaskDTO(BaseModel):
    id: int | None
    title: str
    description: str
    completed: bool = False


@dataclass(slots=True)
class TaskKeys:
    prefix: str = "app"

    @property
    def id(self) -> str:
        return f"{self.prefix}:task:id"

    def task(self, task_id: int) -> str:
        return f"{self.prefix}:task:{task_id}"

    @property
    def index(self) -> str:
        return f"{self.prefix}:task:index"


class TaskRepository(RepositoryABC[TaskDTO]):

    def __init__(self, *, redis_client: Redis.Redis | None = None, prefix: str = "app") -> None:

        self._redis: Redis.Redis = (
            redis_client
            if redis_client is not None
            else Redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)
        )
        self._keys = TaskKeys(prefix)

    @staticmethod
    def _dump(dto: TaskDTO) -> str:
        return dto.model_dump_json()

    @staticmethod
    def _load(raw: str | None) -> TaskDTO | None:
        if not raw:
            return None
        return TaskDTO.model_validate_json(raw)

    async def _mget_many(self, ids: list[int]) -> list[TaskDTO]:
        if not ids:
            return []
        pipe = self._redis.pipeline()
        for i in ids:
            pipe.get(self._keys.task(i))
        raws: list[str | None] = await pipe.execute()
        out: list[TaskDTO] = []
        for raw in raws:
            dto = self._load(raw)
            if dto is not None:
                out.append(dto)
        return out

    async def get_by_id(self, task_id: int) -> TaskDTO | None:
        raw = await self._redis.get(self._keys.task(task_id))
        return self._load(raw)

    async def list(self) -> list[TaskDTO]:
        ids_raw = await self._redis.zrange(self._keys.index, 0, -1)
        ids = [int(x) for x in ids_raw]
        if not ids:
            raise ValueError("There is no tasks in memory")

        pipe = self._redis.pipeline()
        for task_id in ids:
            pipe.get(self._keys.task(task_id))
        raws: list[str | None] = await pipe.execute()

        out: list[TaskDTO] = []
        for raw in raws:
            dto = self._load(raw)
            if dto is not None:
                out.append(dto)

        return out

    async def save(self, dto: TaskDTO) -> TaskDTO:
        new_id = await self._redis.incr(self._keys.id)
        key = self._keys.task(new_id)
        new_dto = dto.model_copy(update={"id": new_id})

        pipe = self._redis.pipeline()
        pipe.set(key, self._dump(new_dto))

        pipe.zadd(self._keys.index, {str(new_id): float(new_id)})
        await pipe.execute()
        return new_dto

    async def update(self, dto: TaskDTO) -> TaskDTO:
        if dto.id is None:
            raise ValueError("Task id is required for update")

        key = self._keys.task(dto.id)
        exists = await self._redis.exists(key)
        if not exists:
            raise ValueError("Task is not exist")

        await self._redis.set(key, self._dump(dto))
        return dto

    async def delete(self, task_id: int) -> bool:
        key = self._keys.task(task_id)
        pipe = self._redis.pipeline()
        pipe.delete(key)
        pipe.zrem(self._keys.index, str(task_id))
        results = await pipe.execute()
        deleted = results[0] if results else 0
        return bool(deleted)