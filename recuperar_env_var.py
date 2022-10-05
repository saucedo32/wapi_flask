import os
from dotenv import load_dotenv

# Cargamos las variables de entorno del proyecto
load_dotenv()

# Guardamos las variables de entorno en una variable
environ_var = os.getenv("WHATSAPP_HOOK_TOKEN")

# Imprimimos la variable de entorno
print(environ_var)


