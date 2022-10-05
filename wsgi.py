# Aqui usaremos el paquete gunicorn para ejecutar la app desarrollada en flask

#from app.main import app
from app import app

if __name__ == "__main__":
    app.run()


# ejecutar la sentencia:
# gunicorn -w 4 wsgi:app
