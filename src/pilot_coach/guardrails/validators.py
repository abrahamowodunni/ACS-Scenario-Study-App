from pilot_coach.guardrails.policies import FORBIDDEN_LIVE_ADVICE_PHRASES
from pilot_coach.shared.exceptions import GuardrailViolationError


def validate_study_only(text: str) -> None:
    lowered = text.lower()
    for phrase in FORBIDDEN_LIVE_ADVICE_PHRASES:
        if phrase in lowered:
            raise GuardrailViolationError("Live flight advice is not allowed in study mode.")
