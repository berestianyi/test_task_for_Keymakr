from pathlib import Path

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from celery.result import AsyncResult

from src.application.shared.celery import celery
from src.application.shared.tasks import fetch_and_save_users_to_csv

user_api_router = APIRouter(prefix="/celery", tags=["TASK_2"])


@user_api_router.post("/fetch-users")
def trigger_fetch_users(url: str | None = Query(default=None)):
    async_result = fetch_and_save_users_to_csv.delay(url=url)
    return {"task_id": async_result.id}


@user_api_router.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    r = AsyncResult(task_id, app=celery)
    return {"task_id": task_id, "state": r.state, "result": r.result if r.successful() else None}


@user_api_router.get("/tasks/{task_id}/download")
def download_by_task(task_id: str):
    r = AsyncResult(task_id, app=celery)
    if not r.successful() or not isinstance(r.result, str):
        raise HTTPException(status_code=404, detail="Not ready")
    return FileResponse(r.result, media_type="text/csv", filename=Path(r.result).name)
