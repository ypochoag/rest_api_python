"""Queries Functions"""


def query_generation(filters: any):
    """Queries Functions"""
    status = ""
    year = ""
    city = ""

    if filters:
        if "status" in filters:
            status = "AND s.name = '" + str(filters["status"]) + "' "
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
        "WHERE s.name in ('vendido', 'en_venta', 'pre_venta')  AND p.price <> 0 " +
        status +
        year +
        city +
        "GROUP BY p.id "
        "ORDER BY p.id")
    return query


def get_data_from_db(cursor: any, filters: any):
    """Queries Functions"""

    query = query_generation(filters)
    cursor.execute(query)
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
            'status': row[6],
        })

    return data
