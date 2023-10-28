"""Modulo para decodificar el archivo .env"""
from decouple import config

DB_HOST = config('DB_HOST', default='localhost')
DB_USER = config('DB_USER', default='usuario')
DB_PORT = config('DB_PORT', default='3030')
DB_PASSWORD = config('DB_PASSWORD', default='contraseña')
DB_NAME = config('DB_NAME', default='nombre_basededatos')
