from fastapi import APIRouter, Depends

from apps.api.dependencies import get_progress_service
from pilot_coach.application.services.progress_service import ProgressService

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/{user_id}")
async def get_progress(
    user_id: str,
    service: ProgressService = Depends(get_progress_service),
) -> dict:
    return await service.get_progress(user_id)
