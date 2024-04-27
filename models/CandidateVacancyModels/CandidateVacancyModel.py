from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    new = "new"
    declined = "declined"
    interesting = "interesting"


class CandidateVacancy(BaseModel):
    candidate_id: int
    vacancy_id: int
    inStatusTime: datetime
    status: Optional[StatusEnum] = None
    resumeMatching: Optional[int] = None
    teamProfileMatch: Optional[int] = None
    recruiterSelection: Optional[bool] = None
    noTelegram: Optional[bool] = None
    interviewPassed: Optional[bool] = None
    frequentJobChanges: Optional[bool] = None
    interviewFailed: Optional[bool] = None
    noHigherEducation: Optional[bool] = None
    experienceMismatch: Optional[bool] = None
    regionMismatch: Optional[bool] = None
    gigaRejected: Optional[bool] = None
    content: Optional[str] = None
