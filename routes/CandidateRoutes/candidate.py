from fastapi import APIRouter
from langchain_community.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

from models.CandidateModels.Candidate import Candidate
from utils import gigachat

candidate_router = APIRouter(prefix='/candidate', tags=['Candidates Stuff'])


@candidate_router.post('/contact')
async def create(candidate: Candidate):
    messages = [SystemMessage(
        content="Ты автоматическая система для распознавания контактных данных из резюме. Укажи в список все контактные данные, которые присутствуют в резюме. Указывай их в строгом формате [название контактной информации]: [контактные данные], без квадратных скобок."),
        HumanMessage(content=candidate.content)]
    messages.append(gigachat.send(messages))
    return messages
