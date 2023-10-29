"""Ejecucion de la aplicacion"""
import http.server
import socketserver
import json
from config.database_config import settings
from db.db_connector import connect_to_db
from db.db_queries import get_data_from_db

db = connect_to_db(settings)
cursor = db.cursor()


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """Class manejar las solicitudes HTTP"""

    def do_GET(self):
        """Function get Request."""
        if self.path == '/api/data':
            # Realiza una consulta a la base de datos
            data = get_data_from_db(cursor, False)

            # Envía la respuesta JSON al cliente
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        else:
            # Si la ruta no coincide con '/api/data', responde con un error 404
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """Function Post Request."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        try:
            # Intenta analizar el JSON recibido
            filters = json.loads(post_data)

            # Obtener los datos filtrtados
            data = get_data_from_db(cursor, filters)

            response = "Datos JSON recibidos con éxito."
        except json.JSONDecodeError:
            response = "Error al analizar los datos JSON."

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


# Inicializa el servidor
PORT = 8000
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Servidor en el puerto", PORT)
    httpd.serve_forever()
