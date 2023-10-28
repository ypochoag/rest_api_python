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

prueba_habi/
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

- `/api/data`: Ruta para acceder a los datos en la base de datos. Puedes filtrar los resultados agregando parámetros a la URL.

