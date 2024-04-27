from typing import Optional

from pydantic import BaseModel

class UserbotModel(BaseModel):
    fio: Optional[str] = None
    phone: Optional[str] = None
    telegram: Optional[str] = None
    content: Optional[str] = None
