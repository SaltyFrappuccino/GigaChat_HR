from fastapi import APIRouter
from fastapi import HTTPException

from database import get_database_connection
from models.CandidateVacancyModels.CandidateVacancyModel import CandidateVacancy

candidate_vacancy_router = APIRouter(tags=['V&C Stuff'])


@candidate_vacancy_router.post("/candidate_vacancies/")
def create_candidate_vacancy(candidate_vacancy: CandidateVacancy):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        # query = "INSERT INTO candidatevacancy (candidate_id, vacancy_id, category) VALUES (%s, %s, %s)"
        query = "INSERT INTO candidatevacancy (candidate_id, vacancy_id, inStatusTime, status, resumeMatching, teamProfileMatch, recruiterSelection, noTelegram, interviewPassed, frequentJobChanges, interviewFailed, noHigherEducation, experienceMismatch, regionMismatch, gigaRejected, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # values = (candidate_vacancy.candidate_id, candidate_vacancy.vacancy_id, candidate_vacancy.category)
        values = (candidate_vacancy.candidate_id, candidate_vacancy.vacancy_id, candidate_vacancy.inStatusTime,
                  candidate_vacancy.status, candidate_vacancy.resumeMatching, candidate_vacancy.teamProfileMatch,
                  candidate_vacancy.recruiterSelection, candidate_vacancy.noTelegram, candidate_vacancy.interviewPassed,
                  candidate_vacancy.frequentJobChanges, candidate_vacancy.interviewFailed, candidate_vacancy.noHigherEducation,
                  candidate_vacancy.experienceMismatch, candidate_vacancy.regionMismatch, candidate_vacancy.gigaRejected, 
                  candidate_vacancy.content)
        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Связь кандидата и вакансии успешно создана"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@candidate_vacancy_router.get("/vacancies_by_candidate/{candidate_id}")
def get_vacancies_by_candidate(candidate_id: int):
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT vacancy.*, candidatevacancy.* FROM vacancy JOIN candidatevacancy ON vacancy.id = candidatevacancy.vacancy_id WHERE candidatevacancy.candidate_id = %s"
        cursor.execute(query, (candidate_id,))
        vacancies = cursor.fetchall()

        cursor.close()
        connection.close()

        return vacancies
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@candidate_vacancy_router.get("/candidates_by_vacancy/{vacancy_id}")
def get_candidates_by_vacancy(vacancy_id: int):
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT candidate.*, candidatevacancy.* FROM candidate JOIN candidatevacancy ON candidate.id = candidatevacancy.candidate_id WHERE candidatevacancy.vacancy_id = %s"
        cursor.execute(query, (vacancy_id,))
        candidates = cursor.fetchall()

        cursor.close()
        connection.close()

        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
