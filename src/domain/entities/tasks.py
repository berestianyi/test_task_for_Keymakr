from dataclasses import dataclass

Title = str
Description = str | None
Completed = bool

@dataclass(kw_only=True)
class Task:
    id: int | None = None
    title: Title
    description: Description
    completed: Completed = False