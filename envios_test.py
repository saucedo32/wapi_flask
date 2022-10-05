import requests
import json
import os
from dotenv import load_dotenv


# Cargamos las variables de entorno del proyecto
load_dotenv()


# Recuperamos las var. de entorno:




#url = "https://graph.facebook.com/v14.0/100417452857527/messages"
url = os.getenv("URL_WAPP")

tel_destino = os.getenv("TEL_DESTINO")
tel_bot = os.getenv("TEL_BOT")
api_token = os.getenv("API_TOKEN")


payload = json.dumps({
  "messaging_product": "whatsapp",
  "to": tel_destino,
  "type": "template",
  "template": {
    "name": "hello_world",
    "language": {
      "code": "en_US"
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  #'Authorization': 'Bearer EAAtOJ6bxteQBABRfsHcdRmzkTblk6sNrRs2Kir95ayv1P2DIVPoN6tSdsGsrzFj8G5R8FujD6ix0pvT7BHrDuZBXO5pLDPsVBqvFmHBmOZAK3ywpGX9KwDXl1n5J601wcbTFOjdZC9qnjdAaJMeNPAH1FTVrp2DHoEQn8M3KjpDZBEcreo2iuerQKz4CM5VsVIeDxZAP1nAZDZD'
  'Authorization': "Bearer " + api_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)




