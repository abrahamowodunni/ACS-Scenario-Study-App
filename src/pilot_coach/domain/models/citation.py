from pydantic import BaseModel


class Citation(BaseModel):
    source_title: str
    section: str | None = None
    page: int | None = None
    acs_code: str | None = None
