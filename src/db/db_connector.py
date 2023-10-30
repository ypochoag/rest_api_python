"""Modulos requeridos"""
import mysql.connector


def connect_to_db(settings: any):
    """Funcion creacion de database conector"""
    try:
        db = mysql.connector.connect(**settings)
        return db
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
