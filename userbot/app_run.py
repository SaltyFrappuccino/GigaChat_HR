from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from pyrogram import Client, filters

dialogues = {}

chatx = GigaChat(
    credentials='ODQ4ODM5MWQtYWViZi00ZGU1LWEzODItMjA5NzRkMDE3Y2VmOmIwNjVmNTA5LTkwMjctNGU5Zi1iZGUwLWU3OWJlNDY3MjcwNg==',
    verify_ssl_certs=False, model="GigaChat-Plus-preview", scope="GIGACHAT_API_CORP")

api_id = 29732919
api_hash = "fdb73b779911302e0161fbbff0bf666f"
number = "+79268740930"

app = Client(name="hr", api_id=api_id, api_hash=api_hash)


@app.on_message(filters=filters.private)
async def chat(event, message):
    chat_id = message.chat.id
    if chat_id not in dialogues:
        dialogues[chat_id] = [SystemMessage(content="Ты рекрутёр в компанию Sber. Твоя задача провести первичное интервьюирование на позицию Junior Java Developer со знаниями в ООП, парадигмах, servlet, gradle и jUnit. Будь очень критичным, отказывай интервьюеру если он неправильно отвечает или плохо разговаривает с тобой. Проверь знания языка Java, знания паттернов, знания ООП, попроси написать код на оценку по ТЗ.")]
    user_input = message.text
    if user_input == "/reset":
        dialogues.pop(chat_id)
    print("User: ", user_input)
    dialogues[chat_id].append(HumanMessage(content=user_input))
    res = chatx(dialogues[chat_id])
    dialogues[chat_id].append(res)
    print("Bot: ", res.content)
    await app.send_message(chat_id, res.content)


app.run()
