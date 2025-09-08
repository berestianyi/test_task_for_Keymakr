from pathlib import Path
import csv
import typing as t
from datetime import datetime, timezone
from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    name: str
    email: str


class UserCSVRepository:

    def save(self, rows: t.List[UserDTO], path: str) -> str:
        out_dir = Path(path)
        out_dir.mkdir(parents=True, exist_ok=True)

        fn = out_dir / f"users_{datetime.now(timezone.utc):%Y%m%d_%H%M%S}.csv"
        with fn.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
            writer.writeheader()
            for r in rows:
                writer.writerow(
                    {
                        "id": r.id,
                        "name": r.name,
                        "email": r.email
                    }
                )
        return str(fn)