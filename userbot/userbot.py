from pyrogram import Client, filters, idle

dialogues = {}

api_id = 29732919
api_hash = "fdb73b779911302e0161fbbff0bf666f"
number = "+79268740930"

app = Client(name="hr", api_id=api_id, api_hash=api_hash)


async def init_message(nickname: str, fio: str, content: str):
    async with Client("hr", api_id, api_hash) as app:
        await app.send_message(nickname, "Вас приветствует HR бот от команды `AI Migos`!")
