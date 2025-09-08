from src.domain.entities.tasks import Title, Description, Completed
from src.use_cases.abc import Input, SuccessfulOutput



class TaskCreateInput(Input):
    title: Title
    description: Description
    completed: Completed



class TaskCreateOutput(SuccessfulOutput):
    id: int
    title: Title
    description: Description
    completed: Completed

