from pydantic import BaseModel

class VacancyUpdate(BaseModel):
    vacancy: str
    content: str
