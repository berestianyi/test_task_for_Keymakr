from dataclasses import dataclass

from src.domain.entities.tasks import Title, Description, Completed
from src.use_cases.abc import Input, SuccessfulOutput


@dataclass(kw_only=True, frozen=True)
class TaskGetListInput(Input):
    pass


@dataclass(kw_only=True, frozen=True)
class TaskGetListOutput(SuccessfulOutput):
    id: int
    title: Title
    description: Description
    completed: Completed

