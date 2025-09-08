from src.domain.entities.users import User
from src.persistence.mapper.CSV.users import UserCSVMapper
from src.persistence.repository.CSV.users import UserCSVRepository
import typing as t

class UserCSVGateway:
    def __init__(self):
        self._repo = UserCSVRepository()
        self._mapper = UserCSVMapper()

    def save(self, *, entities: t.List[User], path: str) -> str:
        dto_list = [self._mapper.to_repository(entity) for entity in entities]
        return self._repo.save(dto_list, path)
