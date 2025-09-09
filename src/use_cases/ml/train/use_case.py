from pathlib import Path
import pandas as pd
from src.application.config import settings
from src.application.shared.ml.pipeline import build_pipeline
from src.persistence.gateway.ml.joblib_model import JoblibModelGateway
from src.use_cases.abc import UseCaseABC
from .ports import TrainModelInput, TrainModelOutput


class TrainModelUseCase(UseCaseABC[TrainModelInput, TrainModelOutput]):
    def __init__(self, model_gateway: JoblibModelGateway | None = None):
        self._gw = model_gateway or JoblibModelGateway()

    def execute(
            self,
            paths: TrainModelInput
    ) -> TrainModelOutput:
        csv_p = Path(paths.csv_path) if paths.csv_path else settings.TASKS_CSV_PATH
        out_p = Path(paths.out_path) if paths.out_path else settings.MODEL_PATH

        df = pd.read_csv(csv_p)
        df.columns = [c.strip().lower() for c in df.columns]
        if not {"task_description", "priority"} <= set(df.columns):
            raise ValueError("CSV must contain columns: task_description, priority")

        X = df["task_description"].astype(str).values
        y = df["priority"].astype(str).str.strip().str.lower().values

        pipe = build_pipeline()
        pipe.fit(X, y)
        return TrainModelOutput(path=self._gw.save(pipe, out_p))
