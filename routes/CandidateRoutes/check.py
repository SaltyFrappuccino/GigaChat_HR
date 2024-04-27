from typing import Annotated

from fastapi import FastAPI, Form, UploadFile, APIRouter
from langchain_core.messages import SystemMessage
from pypdf import PdfReader

from models.CandidateModels.Candidate import Candidate
from utils import gigachat

check_router = APIRouter(prefix="/check", tags=['Utils Stuff'])

@check_router.post("/")
async def check(candidate: Candidate):
    messages = [SystemMessage(content="Ты автоматическая система для распознавания контактных данных из резюме. Укажи в список все контактные данные, которые присутствуют в резюме. Указывай их в строгом формате [название контактной информации]: [контактные данные], без квадратных скобок."), HumanMessage(content=candidate.content)]
    messages.append(gigachat.send(messages))
    return messages

