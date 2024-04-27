from fastapi import APIRouter
from fastapi import HTTPException

from database import get_database_connection
from models.VacancyModels.VacancyModel import Vacancy
from models.VacancyModels.VacancyUpdateModel import VacancyUpdate

vacancies_router = APIRouter(prefix="/vacancies", tags=['Vacancies Stuff'])


@vacancies_router.post("/")
def create_vacancy(vacancy: Vacancy):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "INSERT INTO vacancy (title, positionNumber, manager, recrutor, content) VALUES (%s, %s, %s, %s, %s)"
        values = (vacancy.title, vacancy.positionNumber, vacancy.manager, vacancy.recrutor, vacancy.content)
        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Вакансия успешно создана"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@vacancies_router.get("/")
def get_vacancies(id: int = None):
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        if id is not None:
            cursor.execute("SELECT * FROM vacancy WHERE id = %s ", (id,))
        else:
            cursor.execute(
                "SELECT vacancy.*, COUNT(candidatevacancy.id) as candidates FROM `vacancy` left JOIN candidatevacancy ON vacancy.id = candidatevacancy.vacancy_id GROUP BY vacancy.id")

        vacancies = cursor.fetchall()

        cursor.close()
        connection.close()

        return vacancies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@vacancies_router.put("/{vacancy_id}")
def update_vacancy(vacancy_id: int, vacancy_update: VacancyUpdate):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "UPDATE vacancy SET " + ", ".join(
            f"{field} = %s" for field, value in vacancy_update.dict().items() if value is not None) + " WHERE id = %s"

        values = [value for field, value in vacancy_update.dict().items() if value is not None] + [vacancy_id]

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Вакансия успешно обновлена"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
