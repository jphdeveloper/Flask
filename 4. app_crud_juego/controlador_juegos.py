"""
CRUD FLASK PYTHON + MYSQL
Desarrollado por: Juan Hernandez
"""

# Realizamos la importación de nuestra función de conexión
from bd import obtener_conexion

# Controlador: insertar_juego
def insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
                    (nombre, descripcion, precio))
    conexion.commit()
    conexion.close()

# Controlador: obtener_juegos
def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos
