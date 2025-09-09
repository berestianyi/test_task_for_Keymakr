from dataclasses import dataclass
from pathlib import Path
from src.use_cases.abc import Input, SuccessfulOutput


@dataclass(kw_only=True, frozen=True)
class TrainModelInput(Input):
    csv_path: Path | str | None = None,
    out_path: Path | str | None = None


@dataclass(kw_only=True, frozen=True)
class TrainModelOutput(SuccessfulOutput):
    path: str
