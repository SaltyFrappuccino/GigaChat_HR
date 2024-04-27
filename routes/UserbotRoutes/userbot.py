from fastapi import APIRouter

from models.UserbotModels.UserbotModel import UserbotModel
from userbot.userbot import init_message

userbot_router = APIRouter(prefix="/userbot", tags=["Userbot stuff"])


@userbot_router.post("/")
async def userbot(userbot: UserbotModel):
    await init_message(nickname=userbot.telegram.replace('@', ''), fio=userbot.fio, content=userbot.content)
    return "Started"
