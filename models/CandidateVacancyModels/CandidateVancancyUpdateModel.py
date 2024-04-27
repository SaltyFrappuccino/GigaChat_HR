from typing import Optional

from pydantic import BaseModel


class CandidateVacancyUpdate(BaseModel):
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
    gigacomRejected: Optional[bool] = None
    content: Optional[str] = None
