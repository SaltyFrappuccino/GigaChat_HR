from fastapi import APIRouter
from langchain_community.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

from models.VacancyModels.VacancyCreate import VacancyCreate
from models.VacancyModels.VacancyUpdate import VacancyUpdate
from utils import gigachat

vacancy_router = APIRouter(prefix='/vacancy', tags=['Vacancies Stuff'])

@vacancy_router.post('/')
async def create(vacancy: VacancyCreate):
    messages = [SystemMessage(content="Тебе будет дана информация о какой либо вакансии. Тебе нужно будет составить текст для этой вакансии по шаблону: Название вакансии, Опыт Работы, Требования к кандидату, Будет Плюсом, Условия работы."), HumanMessage(content=vacancy.content)]
    messages.append(gigachat.send(messages))
    return messages


@vacancy_router.post('/update')
async def update(vacancy: VacancyUpdate):
    messages = [SystemMessage(content="Ты помощник для HR отдела, автоматизирующих их работу")]
    messages = [HumanMessage(content="Тебе будет дана вакансия и правка. Внеси праву в вакансию и отправь вакансию с правками.\nВакансия: " + vacancy.vacancy + "\nПравка: " + vacancy.content)]
    messages.append(gigachat.send(messages))
    return messages