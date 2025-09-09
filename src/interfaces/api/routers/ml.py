from fastapi import APIRouter, Depends, HTTPException, status, Response

from src.application.shared.dependency_injection.use_case import get_ml_predict_use_case
from src.application.shared.tasks import train_model_task
from src.interfaces.api.schemas.ml import PredictOut, PredictIn
from src.use_cases.ml.predict.ports import PredictPriorityInput
from src.use_cases.ml.predict.use_case import PredictPriorityUseCase

ml_router = APIRouter(prefix="/ml", tags=["TASK_3"])


@ml_router.post("/train")
def trigger_train():
    r = train_model_task.delay()
    return {"task_id": r.id}


@ml_router.post("/predict", response_model=PredictOut)
def predict(
        data: PredictIn,
        uc: PredictPriorityUseCase = Depends(get_ml_predict_use_case)
):
    try:
        out = uc.execute(PredictPriorityInput(description=data.description))
        return PredictOut(
            priority=out.priority,
            probability=out.probability,
            probs=out.probs
        )
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model is not trained yet. Train it first.")
