from typing import Optional

from pydantic import BaseModel


class Candidate(BaseModel):
    fio: Optional[str] = None
    photo_url: Optional[str] = None
    phone_num: Optional[str] = None
    email: Optional[str] = None
