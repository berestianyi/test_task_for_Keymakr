from dataclasses import dataclass

from src.domain.entities.tasks import Title, Description, Completed
from src.use_cases.abc import Input, SuccessfulOutput


class TaskUpdateInput(Input):
    id: int
    title: Title
    description: Description
    completed: Completed


@dataclass(kw_only=True, frozen=True)
class TaskUpdateOutput(SuccessfulOutput):
    id: int
    title: Title
    description: Description
    completed: Completed

