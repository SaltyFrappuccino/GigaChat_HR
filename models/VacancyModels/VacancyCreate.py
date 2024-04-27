from pydantic import BaseModel


class VacancyCreate(BaseModel):
    content: str
