from typing import Optional

from pydantic import BaseModel


class Vacancy(BaseModel):
    title: str
    positionNumber: Optional[str] = None
    manager: Optional[str] = None
    recrutor: Optional[str] = None
    content: Optional[str] = None
