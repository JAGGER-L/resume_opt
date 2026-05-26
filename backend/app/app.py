from fastapi import FastAPI

from app.api.routes_jobs import router as jobs_router
from app.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(jobs_router)
    return app


app = create_app()
