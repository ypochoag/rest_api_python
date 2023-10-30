"""Levantamiento de servidor"""
import json
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler
from db.db_queries import get_data_from_db
from utils.data_format import data_json_format


class RequestHandler(SimpleHTTPRequestHandler):
    """Clase para manejar las solicitudes HTTP"""

    def do_GET(self):
        """Function get Request."""
        try:
            if self.path == '/api/data':
                # Realiza una consulta a la base de datos
                data = get_data_from_db(False)
                json_data = data_json_format(data)

                # Envía la respuesta JSON al cliente
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(json_data).encode())
            else:
                # Si la ruta no coincide con '/api/data', responde con un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps(
                    {"Error": "Ruta no valida, use: /api/data"}).encode())
        except json.JSONDecodeError:
            self.send_response(500)
            self.end_headers()

    def do_POST(self):
        """Function Post Request."""

        # Habilitacion de filtros
        enable_filter = {
            "status": True,
            "year": True,
            "city": True
        }
        try:
            if self.path == '/api/data':
                content_length = int(self.headers['Content-Length'])
                if content_length > 0:
                    post_data = self.rfile.read(content_length).decode('utf-8')
                    # Intenta analizar el JSON recibido
                    filters = json.loads(post_data)
                    for filter in filters:
                        enable_filter[filter]
                else:
                    filters = 0

                print(filters)

                # Obtener los datos filtrados
                data = get_data_from_db(filters)
                json_data = data_json_format(data)

                # Envía la respuesta JSON al cliente
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(json_data).encode())
            else:
                # Si la ruta no coincide con '/api/data', responde con un error 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps(
                    {"Error": "Ruta no valida, use: /api/data"}).encode())
        except (json.JSONDecodeError, KeyError):
            # Indicar al cliente que los datos enviados no son validos
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps(
                {"Error": "Filtros no validos"}).encode())


# Iniciar el servidor
if __name__ == '__main__':
    PORT = 8000
    with TCPServer(("", PORT), RequestHandler) as httpd:
        print("Servidor en el puerto", PORT)
        httpd.serve_forever()
        httpd.server_close()
        print("Servidor cerrado")
