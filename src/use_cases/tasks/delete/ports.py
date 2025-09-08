from dataclasses import dataclass
from src.use_cases.abc import Input, SuccessfulOutput


@dataclass(kw_only=True, frozen=True)
class TaskDeleteInput(Input):
    id: int


@dataclass(kw_only=True, frozen=True)
class TaskDeleteOutput(SuccessfulOutput):
    is_deleted: bool
