"""Funciones de consulta SQL a DB"""
from db.db_config import SETTINGS
from db.db_connector import connect_to_db


def query_generation(filters: any):
    """Generador de consulta SQL para DB"""
    status = "s.name in ('vendido', 'en_venta', 'pre_venta') "
    year = ""
    city = ""

    if filters:
        if "status" in filters:
            status = "s.name = '" + str(filters["status"]) + "' "
        if "year" in filters:
            year = "AND p.year > " + str(filters["year"]) + " "
        if "city" in filters:
            city = "AND p.city = '" + str(filters["city"]) + "' "

    query = (
        "SELECT p.id, p.address, p.city, p.price, "
        "p.description, p.year, s.name, max(sh.update_date) "
        "FROM property p "
        "INNER JOIN status_history sh "
        "ON p.id = sh.property_id "
        "INNER JOIN status s "
        "ON s.id = sh.status_id "
        "WHERE " + status + "AND p.price <> 0 " +
        year +
        city +
        "GROUP BY p.id "
        "ORDER BY p.id")
    return query


def get_data_from_db(filters: any):
    """Apertura, consulta y cierre de DB"""

    # Requerir punto de conexion a DB
    db = connect_to_db(SETTINGS)
    if not db:
        return False

    # Generar requerimiento en SQL
    query = query_generation(filters)

    # Realizar consulta a DB
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # Cierre de conexión DB
    cursor.close()
    db.close()

    return data
