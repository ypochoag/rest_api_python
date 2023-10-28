"""Ejecucion de la aplicacion"""
import http.server
import socketserver
import json
from config.database_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
from db.db_connector import connect_to_db

db = connect_to_db(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)
cursor = db.cursor()


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """Class manejar las solicitudes HTTP"""

    def do_GET(self):
        print("Ruta", self.path)
        if self.path == '/api/data':
            # Realiza una consulta a la base de datos
            cursor.execute("SELECT * FROM property")
            result = cursor.fetchall()

            # Convierte el resultado de la consulta a formato JSON
            data = []
            for row in result:
                data.append({
                    'id': row[0],
                    'address': row[1],
                    'city': row[2],
                    'price': row[3],
                    'description': row[4],
                    'year': row[5],
                    # Agrega más campos según tu esquema
                })

            # Envía la respuesta JSON al cliente
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        else:
            # Si la ruta no coincide con '/api/data', responde con un error 404
            self.send_response(404)
            self.end_headers()


# Inicializa el servidor
PORT = 8000
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Servidor en el puerto", PORT)
    httpd.serve_forever()
