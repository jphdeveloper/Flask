#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host="localhost",  # Cambia esto si tu servidor no está en localhost
        user="root",  # Tu usuario de MySQL
        password="",  # Tu contraseña de MySQL
        database="app_crud_juego"  # El nombre exacto de la base de datos
    )
    return mydb

    '''       
    if mydb:
        return ("Conexion exitosa")
    else:
        return ("Error en la conexion a BD")
    '''
    
    