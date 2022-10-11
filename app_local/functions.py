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
token = os.getenv("WHATSAPP_API_TOKEN")


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
  'Authorization': token
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)



def envio_mensaje(tel_destino, mensaje):
  payload = json.dumps({
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": tel_destino,
  "type": "text",
  "text": {
    "preview_url": False,
    "body": mensaje
    }
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': token
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)



# Defino funcion para cargar datos del json:
def cargar_json(ruta):
    with open(ruta) as contenido:
        resultado = json.load(contenido)
        return resultado









