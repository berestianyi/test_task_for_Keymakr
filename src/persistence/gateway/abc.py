import typing as t
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Entity:
    pass


SomeEntity = t.TypeVar(
    "SomeEntity",
    bound=Entity,
)


class GatewayABC(ABC, t.Generic[SomeEntity]):

    @abstractmethod
    async def get_by_id(self, index: int) -> SomeEntity:
        pass

    @abstractmethod
    async def list(self) -> t.List[SomeEntity]:
        pass

    @abstractmethod
    async def save(self, entity: SomeEntity) -> SomeEntity:
        pass

    @abstractmethod
    async def update(self, entity: SomeEntity) -> SomeEntity:
        pass

    @abstractmethod
    async def delete(self, index: int) -> bool:
        pass
