""""
CRUD FLASK PYTHON + MYSQL
Desarrollado po: Juan Hernandez
"""
#Realizamos la importacion de la libreria con pup install
import pymysql

#Configuramos los datos de conexion con la base de datos
def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='app_crud_juego')