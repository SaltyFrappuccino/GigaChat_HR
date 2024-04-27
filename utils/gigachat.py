from langchain_community.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

from utils.config import auth_data, scope, model


def create():
    return GigaChat(credentials=auth_data, verify_ssl_certs=False, scope=scope, model=model)


def send(messages):
    chat = create()
    return chat(messages)
