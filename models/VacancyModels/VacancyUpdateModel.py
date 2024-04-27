from typing import Optional

from pydantic import BaseModel


class VacancyUpdate(BaseModel):
    title: Optional[str] = None
    positionNumber: Optional[str] = None
    manager: Optional[str] = None
    recrutor: Optional[str] = None
    content: Optional[str] = None
