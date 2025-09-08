import typing as t
from abc import ABC, abstractmethod
from pydantic import BaseModel


class DTO(BaseModel):
    pass


SomeDTO = t.TypeVar(
    "SomeDTO",
    bound=DTO,
)


class RepositoryABC(ABC, t.Generic[SomeDTO]):

    @abstractmethod
    async def get_by_id(self, index: int) -> SomeDTO:
        pass

    @abstractmethod
    async def list(self) -> t.List[SomeDTO]:
        pass

    @abstractmethod
    async def save(self, dto: SomeDTO) -> SomeDTO:
        pass

    @abstractmethod
    async def update(self, dto: SomeDTO) -> SomeDTO:
        pass

    @abstractmethod
    async def delete(self, index: int) -> bool:
        pass
