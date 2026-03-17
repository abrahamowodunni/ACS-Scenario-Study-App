from fastapi import APIRouter

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/")
async def list_sessions() -> dict[str, list]:
    return {"sessions": []}
