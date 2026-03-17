from pilot_coach.domain.ports.session_repository_port import SessionRepositoryPort


class ProgressService:
    def __init__(self, session_repository: SessionRepositoryPort) -> None:
        self.session_repository = session_repository

    async def get_progress(self, user_id: str) -> dict:
        return await self.session_repository.get_progress(user_id)
