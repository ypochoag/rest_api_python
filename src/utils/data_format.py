"""Funciones de conversion de datos a formatos especificos"""


def data_json_format(raw_data: any):
    """Ajuste de datos a formato JSON"""

    # Convertir el resultado de la consulta a formato JSON
    data = []
    for row in raw_data:
        data.append({
            'id': row[0],
            'address': row[1],
            'city': row[2],
            'price': row[3],
            'description': row[4],
            'year': row[5],
            'status': row[6],
        })
    return data
