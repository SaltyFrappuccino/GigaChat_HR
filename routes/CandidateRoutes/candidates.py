from fastapi import APIRouter
from fastapi import HTTPException

from database import get_database_connection
from models.CandidateModels.Candidate import Candidate
from models.CandidateVacancyModels.CandidateVancancyUpdateModel import CandidateVacancyUpdate

candidates_router = APIRouter(prefix="/candidates", tags=['Candidates Stuff'])


@candidates_router.post("/")
def create_candidate(candidate: Candidate):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        # query = "INSERT INTO candidate (fio, inStatusTime, status, resumeMatching, teamProfileMatch, recruiterSelection, noTelegram, interviewPassed, frequentJobChanges, interviewFailed, noHigherEducation, experienceMismatch, regionMismatch, gigaRejected, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        query = "INSERT INTO candidate (fio, photo_url, phone_num, email) VALUES (%s, %s, %s, %s)"
        # values = (candidate.fio, "10-10-2023", candidate.status, candidate.resumeMatching, candidate.teamProfileMatch,
        #           candidate.recruiterSelection, candidate.noTelegram, candidate.interviewPassed,
        #           candidate.frequentJobChanges, candidate.interviewFailed, candidate.noHigherEducation,
        #           candidate.experienceMismatch, candidate.regionMismatch, candidate.gigaRejected, candidate.content)
        values = (candidate.fio, candidate.photo_url, candidate.phone_num, candidate.email)
        cursor.execute(query, values)
        cursor.execute("SET @person_id = LAST_INSERT_ID()")
        cursor.execute("SELECT id from vacancy")

        vacancies_id = cursor.fetchall()
        for i in vacancies_id:
            cursor.execute("INSERT INTO candidatevacancy (candidate_id, vacancy_id) VALUES (@person_id, %s)", i)

        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Кандидат успешно создан"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@candidates_router.get("/")
def get_candidates(id: int = None):
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        if id is not None:
            cursor.execute("SELECT * FROM candidate WHERE id = %s", (id,))
        else:
            cursor.execute("SELECT * FROM candidate")

        candidates = cursor.fetchall()

        cursor.close()
        connection.close()

        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@candidates_router.put("/{candidate_id}")
def update_candidate(candidate_id: int, candidate_update: Candidate):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "UPDATE candidate SET " + ", ".join(
            f"{field} = %s" for field, value in candidate_update.dict().items() if value is not None) + " WHERE id = %s"

        values = [value for field, value in candidate_update.dict().items() if value is not None] + [candidate_id]

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Кандидат успешно обновлен"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
