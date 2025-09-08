from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.application.config import settings
from src.interfaces.api.routers.tasks import task_router


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

    return app