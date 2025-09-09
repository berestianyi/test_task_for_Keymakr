from typing import Dict, Any
from sklearn.pipeline import Pipeline
from src.application.config import settings
from src.persistence.gateway.ml.joblib_model import JoblibModelGateway
from src.use_cases.abc import UseCaseABC
from .ports import PredictPriorityInput, PredictPriorityOutput


class PredictPriorityUseCase(UseCaseABC[PredictPriorityInput, PredictPriorityOutput]):

    def __init__(self, model_gateway: JoblibModelGateway, ):
        self._gw = model_gateway

    def _get_model(self) -> Pipeline:
        return self._gw.load(settings.MODEL_PATH)

    def execute(self, ml_input: PredictPriorityInput) -> PredictPriorityOutput:
        text = ml_input.description.strip()
        if not text:
            raise ValueError("Description is empty")

        model = self._get_model()
        prediction = model.predict([text])[0]
        resp: Dict[str, Any] = {"priority": str(prediction), "probability": 1.0, "probs": {}}

        if hasattr(model, "predict_proba"):
            arr = model.predict_proba([text])[0]
            classes = getattr(model, "classes_", [])
            probs = {str(c): float(p) for c, p in zip(classes, arr)}
            resp["probs"] = probs
            resp["probability"] = probs.get(str(prediction), float(max(arr)))

        return PredictPriorityOutput(
            priority=resp.get("priority"),
            probability=resp.get("probability"),
            probs=resp.get("probs")
        )