from .abc import ToDomainMapper, ToRepositoryMapper
from src.persistence.repository.tasks import TaskDTO
from src.domain.entities.tasks import Task


class TaskMapper(
    ToDomainMapper[Task, TaskDTO],
    ToRepositoryMapper[Task, TaskDTO],
):
    def to_domain(self, repository_entity: TaskDTO) -> Task:
        return Task(
            id=repository_entity.id,
            title=repository_entity.title,
            description=repository_entity.description,
            completed=repository_entity.completed
        )

    def to_repository(self, domain_entity: Task) -> TaskDTO:
        return TaskDTO(
            id=domain_entity.id,
            title=domain_entity.title,
            description=domain_entity.description,
            completed=domain_entity.completed,
        )
