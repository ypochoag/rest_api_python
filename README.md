# Proyecto API Habi

Este proyecto tiene como objetivo proporcionar a los usuarios una herramienta eficiente para consultar inmuebles disponibles y vendidos en el mercado mediante una API Rest. La aplicación permitirá a los usuarios explorar un listado de propiedades, brindando acceso a información detallada sobre cada una. Para facilitar la búsqueda, los usuarios podrán aplicar diversos filtros, como año de construcción, ciudad y estado. Con esta herramienta, se simplifica la experiencia de búsqueda de inmuebles, brindando a los usuarios la capacidad de tomar decisiones informadas en el proceso de compra de propiedades.

## Tecnologías Utilizadas

- Python: Lenguaje de programación utilizado para desarrollar la API.
- MySQL: Sistema de gestión de bases de datos utilizado para almacenar y recuperar datos.
- `mysql-connector-python`: Biblioteca Python para interactuar con la base de datos MySQL.
- `python-decouple`: Biblioteca para gestionar las configuraciones y variables de entorno de la aplicación.

## Configuración de Base de Datos

Asegúrate de configurar adecuadamente la base de datos en un archivo `.env`. Se proporciona un Ejemplo de un archivo en `.env.example`.


## Desarrollo

### Estructura de Carpetas

La estructura de carpetas del proyecto se organiza de la siguiente manera:

prueba_habi/│
├──src
  │
  ├── api_habi.py
  ├── db/
  │ ├── init.py
  │ └── db_connector.py
  │
  ├── routes/
  │ ├── init.py
  │ └── data_routes.py
  │
  └── config/
    ├── init.py
    ├── database_config.py
    └── .env.example


- **`api_habi.py`**: El archivo principal de la API que maneja las solicitudes HTTP.
- **`db/`**: Contiene los archivos relacionados con la base de datos, como la lógica de conexión.
- **`routes/`**: Define las rutas de la API para datos y diferentes recursos que se requieran posteriormente.
- **`config/`**: Almacena configuraciones y variables de entorno.

### Ejecución

Para ejecutar el proyecto:

1. Asegúrate de tener Python instalado en tu entorno.
2. Instala las dependencias utilizando `pip install mysql-connector-python python-decouple`.
3. Crea un archivo `.env` con la configuración de la base de datos.
4. Ejecuta el proyecto con `python api_habi.py`.

### Rutas de API

- `/api/data`: Ruta para acceder a los datos en la base de datos. Para acceder a la base de datos se pueden hacer dos requerimientos GET y POST.

### Método GET: 
Se puede acceder a la lista de propiedades en estado "pre_venta", "en_venta" y "vendido" utilizando el endpoint descrito anteriormente. 

Nota: En caso que se este ejecutando en una maquina local el punto de acceso sera el siguiente:

`GET` : <http://localhost:8000/api/data>

```javascript
[
    {
        "id": 1,
        "address": "calle 23 #45-67",
        "city": "bogota",
        "price": 120000000,
        "description": "Hermoso apartamento en el centro de la ciudad",
        "year": 2000,
        "status": "pre_venta"
    },
    {
        "id": 2,
        "address": "carrera 100 #15-90",
        "city": "bogota",
        "price": 350000000,
        "description": "Amplio apartamento en conjunto cerrado",
        "year": 2011,
        "status": "en_venta"
    },
    ...
]    
```


### Método POST:
Con el fin de satisfacer los requisitos de filtrado que se originen desde el frontend, se ha implementado el método POST en el mismo endpoint anterior. 

Parametros disponibles para filtrado:

|     Name      | Tipo de dato  | Descripción  |
| ------------- | ------------- |------------- |
| Status | String | Estado de la propiedad ["pre_venta", "en_venta", "vendido"]  |
| year | Int  | Año de construcción | 
| city | String  | Ciudad donde se encuentra la propiedad |


En este método, se debe proporcionar en el body un archivo en formato JSON como el siguiente:

```javascript
body = {   
    "status": "pre_venta",
    "year": 2019,
    "city": "Bogota" 
}
```

`POST` : <http://localhost:8000/api/data>

```javascript
[
    {
        "id": 10,
        "address": "calle 95 # 78 - 49",
        "city": "bogota",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar",
        "year": 2020,
        "status": "pre_venta"
    },
    {
        "id": 67,
        "address": "calle 95 # 78 - 123",
        "city": "bogota",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar",
        "year": 2020,
        "status": "pre_venta"
    }
]    
```

## Servicio de "Me gusta"

Se implementa una actualización en la base de datos para permitir que los usuarios registrados expresen su aprobación mediante un like a sus propiedades favoritas. Estas interacciones se registrarán con una marca de tiempo (DATETIME).

A continuación, se presenta el Diagrama de Entidad-Relación, que se desarrolló de la siguiente manera:

1. Entidades :
	 Creación de nuevas entidades junto con los atributos correspondientes:
	 - La entidad "user" incluye los atributos de los usuarios registrados.
	 - Dado que se requiere registrar la interaccion entre las entidades usuarios y propiedades mediante likes, se propone la creación de la entidad "like_history", en la cual se registrarán los momentos en que un usuario da "Me gusta" a una propiedad.
	 - Como mejora, se sugiere crear la entidad "city," que almacenará todas las ciudades con una identificación única (ID). Esto permitirá a los usuarios seleccionar una ciudad de una lista de opciones en lugar de tener que escribir el nombre de la ciudad. Además, facilitará mantener referencias a las ciudades en los registros de usuarios.

2. Relaciones
Las relaciones serían las siguientes:
- Un usuario puede dar "Me gusta" a varios productos, por lo que tendría una relación uno a muchos entre "user" y "like_history".
- Un producto puede recibir "Me gusta" de varios usuarios, por lo que también tendría una relación uno a muchos entre "property" y "like_history".
- Un usuario se puede registrar en una ciudad, por lo que tendria una relación de uno a muchos entre "user" y "city".
- Una propiedad puede registrarse en  una ciudad, por lo que tendría una relacion de uno a muchos entre "property" y "city".

#### Diagrama de entidad - relación
![](https://github.com/ypochoag/rest_api_python/blob/main/me_gusta/dig_er_habi_me_gusta.png?raw=true)

### Codigo SQL
Para la implementacion del planteamiento anterior se propone un script en SQL con la creacion de las nuevas entidades y su respectivo enlace a la base de datos. 
[Ver codigo](https://github.com/ypochoag/rest_api_python/blob/main/me_gusta/sql_implementacion_me_gusta.sql)