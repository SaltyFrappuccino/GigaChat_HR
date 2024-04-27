import json
import uuid

from utils.config import auth_data, scope

AUTH_DATA = auth_data
SCOPE = scope
DEBUG = True

import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = 'scope=' + SCOPE
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': str(uuid.uuid4()),
    'Authorization': 'Basic ' + AUTH_DATA
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
token = response.json()['access_token']

messages = []
message_assistant = {'role': 'system',
                     'content': ''}
message = {'role': 'user', 'content': 'Какая погода в Москве?'}
if message_assistant not in messages:
    messages.extend([message_assistant, message])
else:
    messages.append(message)
url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
payload = json.dumps({
    "model": "GigaChat-Plus-preview",
    "messages": messages,
    "max_tokens": 512,
    "function_call": "auto",
    "functions": [{
        "name": "weather_forecast",
        "description": "Возвращает температуру на заданный период",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Местоположение, например, название города"
                },
                "format": {
                    "type": "string",
                    "enum": [
                        "celsius",
                        "fahrenheit"
                    ],
                    "description": "Единицы изменерия температуры"
                },
                "num_days": {
                    "type": "integer",
                    "description": "Период, для которого нужно вернуть"
                }
            },
            "required": [
                "location",
                "num_days"
            ]
        },
        "few_shot_examples": [
            {
                "request": "Какая погода в моске в ближайшие три дня",
                "params": {
                    "location": "Moscow, Russia",
                    "format": "celsius",
                    "num_days": "3"
                }
            }
        ],
        "return_parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Местоположение, например, название города"
                },
                "temperature": {
                    "type": "integer",
                    "description": "Температура для заданного местоположения"
                },
                "forecast": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Описание погодных условий"
                },
                "error": {
                    "type": "string",
                    "description": "Возвращается при возникновении ошибки. Содержит описание ошибки"
                }
            }
        }
    }]
})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + token,
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.json())
role = response.json()['choices'][0]['message']['role']
content = response.json()['choices'][0]['message']['content']
message = {'role': role, 'content': content}
messages.append(message)
print(messages)
