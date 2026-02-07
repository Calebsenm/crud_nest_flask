from dotenv import load_dotenv
from os import environ
from psycopg2 import connect

load_dotenv()

#Crendenciales de postgres
host =  environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname = environ.get('DB_DATABASE')
username = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')

#Funcion para conectar a la base de datos 
def get_connection():
    try:
        conn = connect(
            host=host,
            user=username,
            password=password,
            database = dbname,
            port=port
        )

        print("Conexion exitosa")
        return conn 
    
    except Exception as ex:
        print("Error de conexion")
        print(ex)