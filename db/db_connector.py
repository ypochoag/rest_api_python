"""Modulos requeridos"""
import mysql.connector

def connect_to_db(db_host: any, db_port:any, db_user: any, db_password: any, db_name: any):
    """Funcion creacion de database conector"""
    try:
        db = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )
        return db
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
