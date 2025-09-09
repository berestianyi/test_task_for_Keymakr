from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.staticfiles import StaticFiles

from src.application.config import settings
from src.interfaces.api.routers.ml import ml_router
from src.interfaces.api.routers.tasks import task_router
from src.interfaces.api.routers.users import user_api_router


def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(task_router)
    app.include_router(user_api_router)
    app.include_router(ml_router)

    app.mount("/files/csv", StaticFiles(directory=settings.USERS_CSV_PATH, check_dir=True), name="csv")
    return app