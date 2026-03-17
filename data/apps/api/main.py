from fastapi import FastAPI

from apps.api.config import APP_NAME
from apps.api.routers.health import router as health_router
from apps.api.routers.scenarios import router as scenarios_router
from apps.api.routers.sessions import router as sessions_router
from apps.api.routers.evaluation import router as evaluation_router
from apps.api.routers.progress import router as progress_router


app = FastAPI(title=APP_NAME)

app.include_router(health_router)
app.include_router(scenarios_router)
app.include_router(sessions_router)
app.include_router(evaluation_router)
app.include_router(progress_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Pilot ACS Coach API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("apps.api.main:app", host="127.0.0.1", port=8000, reload=False)
