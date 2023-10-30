"""Modulo para decodificar el archivo .env"""
from decouple import config

DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default='3030')
DB_USER = config('DB_USER', default='usuario')
DB_PASSWORD = config('DB_PASSWORD', default='contraseña')
DB_NAME = config('DB_NAME', default='nombre_basededatos')

SETTINGS = {
    "host": DB_HOST,
    "port": DB_PORT,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME,
}
