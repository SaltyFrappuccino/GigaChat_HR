from pyrogram import Client, filters, idle

dialogues = {}

api_id = 29732919
api_hash = "fdb73b779911302e0161fbbff0bf666f"
number = "+79268740930"
session_string = "AgHFsDcAAoNVE-APZpdOuumKkFga9i0jdptoOJ5dLDkz6vUdYUz7fvxpoEcYsco5inCSRtGe3GFkPpgw-x0bD3O5nj7YMVA-TFWoJKeLNvD_796-DJ7OSii59MoCeGEUyuBhoyQRrsy410sIvDQB18tu5jYQKeTDjkJBbmFGGijgkHydgbgkvk6o1uwQFGJyGGDjTT6qCLhA91VDzu_qT_5lmJMwR9QYUfJ7EYbXi89GVNB_3cGkYsY1rUsAntXvaHGi_wYjPdCyBNxVXj5LFtHopMTicVB454msi9a3QO9zGPz5z-DXfxRMVnCbd2Rc7MiSMMgevb-MSRxs6SASjRFS0bXXKAAAAAGqXtiTAA"

app = Client(name="hr", api_id=api_id, api_hash=api_hash)


async def init_message(nickname: str, fio: str, content: str):
    async with Client("hr", api_id, api_hash, session_string=session_string) as app:
        await app.send_message(nickname, "Вас приветствует HR бот от команды `AI Migos`!")

