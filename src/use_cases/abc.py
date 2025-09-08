import typing as t
from abc import ABC, abstractmethod
from pydantic import BaseModel



class Input(BaseModel):
    pass



class SuccessfulOutput(BaseModel):
    pass



SomeInput = t.TypeVar("SomeInput", bound=Input)
SomeOutput = t.TypeVar(
    "SomeOutput",
    bound=SuccessfulOutput,
)


class UseCaseABC(ABC, t.Generic[SomeInput, SomeOutput]):
    @abstractmethod
    async def execute(self, some_input: SomeInput) -> SomeOutput:
        raise NotImplementedError("Usecase.execute() must be implemented")

class NoInputUseCaseABC(ABC, t.Generic[SomeOutput]):
    @abstractmethod
    async def execute(self) -> SomeOutput:
        raise NotImplementedError("Usecase.execute() must be implemented")