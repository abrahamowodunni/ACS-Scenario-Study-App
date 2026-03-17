class PilotCoachError(Exception):
    """Base exception for the application."""


class MissingConfigurationError(PilotCoachError):
    """Raised when required configuration is missing."""


class GuardrailViolationError(PilotCoachError):
    """Raised when output or request violates study policies."""
