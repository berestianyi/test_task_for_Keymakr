from dataclasses import dataclass

from src.use_cases.abc import Input, SuccessfulOutput


@dataclass(kw_only=True, frozen=True)
class PredictPriorityInput(Input):
    description: str


@dataclass(kw_only=True, frozen=True)
class PredictPriorityOutput(SuccessfulOutput):
    priority: str
    probability: float
    probs: dict
