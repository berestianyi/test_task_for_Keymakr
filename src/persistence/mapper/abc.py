import typing as t
from abc import abstractmethod, ABC

SomeDomainEntity = t.TypeVar("SomeDomainEntity")
SomeRepositoryEntity = t.TypeVar("SomeRepositoryEntity")


class ToDomainMapper(
    ABC, t.Generic[SomeDomainEntity, SomeRepositoryEntity]
):
    @abstractmethod
    def to_domain(
        self, repository_entity: SomeRepositoryEntity
    ) -> SomeDomainEntity:
        pass


class ToRepositoryMapper(
    ABC, t.Generic[SomeDomainEntity, SomeRepositoryEntity]
):
    @abstractmethod
    def to_repository(
        self, domain_entity: SomeDomainEntity
    ) -> SomeRepositoryEntity:
        pass
