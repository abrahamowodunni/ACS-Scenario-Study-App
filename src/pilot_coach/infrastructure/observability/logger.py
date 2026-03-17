import logging

from pilot_coach.shared.settings import settings


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
    return logging.getLogger(name)
