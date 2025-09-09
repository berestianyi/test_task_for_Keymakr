from pydantic import BaseModel


class PredictIn(BaseModel):
    description: str

class PredictOut(BaseModel):
    priority: str
    probability: float
    probs: dict