## FUENTES DE INFORMACION:

# Foro para app: https://koladev.xyz/posts/flask-whatsapp-cloud-api-1/
# YT explicando paquete dotenv: 

# Importamos las librerias necesarias:
import os
from flask import Flask, jsonify, request
from app.whatsapp_client import WhatsAppWrapper  # Cliente definido que se encuentra en la carpeta app

# El siguiente script es para crear la app web con flask:

app = Flask(__name__)

# Token de verificacion del hook fb:
VERIFY_TOKEN = os.environ.get('WHATSAPP_HOOK_TOKEN')


# Dentro del "home" nos debe saludar
@app.route("/")
def hello_world():
    return "Hola, estoy en el home!"


## Dentro de /send_template_message/ debe enviar el mensaje de prueba
#@app.route("/send_template_message/", methods=["POST"])
#def send_template_message():
#    pass











