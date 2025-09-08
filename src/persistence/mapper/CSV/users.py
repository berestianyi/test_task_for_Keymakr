from src.persistence.mapper.abc import ToDomainMapper, ToRepositoryMapper
from src.persistence.repository.CSV.users import UserDTO
from src.domain.entities.users import User


class UserCSVMapper(
    ToDomainMapper[User, UserDTO],
    ToRepositoryMapper[User, UserDTO],
):
    def to_domain(self, repository_entity: UserDTO) -> User:
        return User(
            id=repository_entity.id,
            name=repository_entity.name,
            email=repository_entity.email,
        )

    def to_repository(self, domain_entity: User) -> UserDTO:
        return UserDTO(
            id=domain_entity.id,
            name=domain_entity.name,
            email=domain_entity.email,
        )
