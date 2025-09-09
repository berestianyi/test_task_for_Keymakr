from pathlib import Path
from joblib import dump, load
from sklearn.pipeline import Pipeline


class JoblibModelGateway:
    def save(self, model: Pipeline, path: Path | str) -> str:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        dump(model, p)
        return str(p)

    def load(self, path: Path | str) -> Pipeline:
        return load(Path(path))