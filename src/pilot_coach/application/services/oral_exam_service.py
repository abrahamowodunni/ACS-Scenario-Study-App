class OralExamService:
    async def ask_followup(self, current_answer: str) -> str:
        return (
            "What regulation, risk factor, or practical consideration supports that answer?"
        )
