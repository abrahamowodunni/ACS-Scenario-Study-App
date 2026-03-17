from pilot_coach.domain.ports.session_repository_port import SessionRepositoryPort


class SQLiteSessionRepository(SessionRepositoryPort):
    async def get_progress(self, user_id: str) -> dict:
        return {
            "user_id": user_id,
            "sessions_completed": 0,
            "weak_areas": [],
            "latest_score": None,
        }
