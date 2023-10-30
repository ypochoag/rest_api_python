"""Test de la funcion GET"""
import unittest
import threading
import json
from http.server import HTTPServer
import requests
from api_habi import RequestHandler


class TestApiHabi(unittest.TestCase):
    """Class test de la api"""

    def setUp(self):
        self.server = HTTPServer(('localhost', 8080), RequestHandler)
        self.server.timeout = 0.01  # Reducir el tiempo de espera para las pruebas
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def test_get_good_route(self):
        """Prueba de la funcion get al endpoint de la API"""
        response = requests.get('http://localhost:8080/api/data', timeout=2000)
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        current_response = {
            "list": type(json_data),
            "dist": type(json_data[0]),
        }
        good_response = {
            "list": list,
            "dist": dict,
        }
        self.assertEqual(current_response, good_response)

    def test_get_bad_route(self):
        """Prueba de la funcion get a otra ruta"""
        response = requests.get(
            'http://localhost:8080/api/data/other', timeout=2000)
        self.assertEqual(response.status_code, 404)
        good_response = '{"Error": "Ruta no valida, use: /api/data"}'
        self.assertEqual(response.text, good_response)

    def test_post_good_route(self):
        """Prueba de la funcion post al endpoint de la API"""
        datos = {
            "status": "pre_venta",
            "year": 2019,
            "city": "bogota"
        }
        current_response = True
        response = requests.post(
            'http://localhost:8080/api/data', json=datos, timeout=2000)
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        for property in json_data:
            if (property['status'] != datos['status']
                or property['year'] < datos['year']
                    or property['city'] != datos['city']):
                current_response = False
                print(property)

        good_response = True
        self.assertEqual(current_response, good_response)

    def test_post_bad_route(self):
        """Prueba de la funcion post a otra ruta"""
        response = requests.post(
            'http://localhost:8080/api/data/other', timeout=2000)
        self.assertEqual(response.status_code, 400)
        good_response = '{"Error": "Filtros no validos"}'
        self.assertEqual(response.text, good_response)


if __name__ == '__main__':
    unittest.main()
