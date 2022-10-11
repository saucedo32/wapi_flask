# Para enviar mensajes debemos prebiamente recibir uno del otro lado.
# No alcanza con el envío del template:

import requests
import json
import os


from dotenv import load_dotenv
# Cargamos las variables de entorno del proyecto
load_dotenv()
api_token = os.getenv("WHATSAPP_API_TOKEN")





url = "https://graph.facebook.com/v14.0/100417452857527/messages"

payload = json.dumps({
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": 543492575809,
  "type": "text",
  "text": {
    "preview_url": False,
    "body": "Vamo' lo pibe"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': api_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)