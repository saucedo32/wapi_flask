# DEFINICION DE FUNCIONES PARA PRUEBA.

# Comun a todas las funciones:
import requests
import json
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno del proyecto
load_dotenv()

#url = "https://graph.facebook.com/v14.0/100417452857527/messages"
url = os.getenv("URL_WAPP")
#tel_destino = os.getenv("TEL_DESTINO")
tel_bot = os.getenv("TEL_BOT")
api_token = os.getenv("API_TOKEN")


# 1- Envio de templates:

def envio_template(tel_destino, template_name, template_idiom):

    #tel_destino = tel_destino

    payload = json.dumps({
    "messaging_product": "whatsapp",
    "to": tel_destino,
    "type": "template",
    "template": {
        "name": template_name,
        "language": {
        "code": template_idiom
        }
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer EAAtOJ6bxteQBAHDrRM58a4jH7zs7woX9RJZC5M996zdHzIsx0IElm8B0iZBQ5hZAgz2EH7xpZBOr0cLwrGaJKu7JKJZAsjuBLZAn3QyNfpFa6xYHnNNrEpr8FYcOOsczDbbp6UlM6gptAxBGAPWVfS6p68t7keCmKuTBkdAKB0fJI8yw4ZChIQtWIsv1Y8IHyZCgkASulwGxegZDZD'
    #'Authorization': "Bearer " + api_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


