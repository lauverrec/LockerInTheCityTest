# LockerInTheCity

Este proyecto es la solución para la prueba técnica *LockerInTheCity*. El objetivo es modelar y mantener una base de datos que nos permita comparar sencillamente valores
calóricos, de grasas saturadas y de azúcar de distintos productos comestibles así como el
diferente precio de cada producto en distintos establecimientos.

## Requisitos
- Docker y Docker Compose
- Python 3.8+
- Dependencias de Python, estas se encuentran definidas en el fichero requirements.txt

## Estructura del Proyecto

    LockerInTheCityTest/
    ├── api/
    │   ├── databaseConnection.py         # Configuración de la conexión a la BD
    │   ├── models.py                     # Modelos de la BD (SQLAlchemy)
    │   ├── schemas.py                    # Esquemas de validación (Pydantic)
    │   └── main.py                       # Definición de la API (FastAPI)
    ├── database/
    │   ├── init.sql                      # Configuración del usuario user
    │   ├── schema.sql                    # Esquema de la base de datos
    ├── docker/
    │ └── docker-compose.yml              # Configuración para levantar MySQL en Docker
    ├── initial_set.py                    # Genera archivos CSV con datos iniciales
    ├── load_data.py                      # Carga los datos a la BD a través de la API
    ├── README.md                         # Este archivo
    └── requirements.txt                  # Archivo que contiene las dependencias


## Pasos para ejecutar el sistema

En primer lugar, vamos a crear un entorno virtual. Desde la raíz del proyecto ejecuta lo siguiente:

```bash
    python -m venv venv
```
Esto creará una carpeta llamada *venv*, este nombre se puede cambiar por el que se quiera.

Para activar el entorno virtual, ejecutamos lo siguiente:
* En **Linux**
```bash
    source venv/bin/activate
```

* En **Window**

```bash
    venv\Scripts\activate
```

Instalamos las dependencias:

```bash
    pip install -r requirements.txt
```

Para desactivar el entorno virtual, ejecutamos:

```bash
    deactivate
```

1. **Levantar la base de datos:**

    Desde la raíz del proyecto, ejecuta:

```bash
    cd docker
    docker-compose up -d
```


2. **Generar el set de datos iniciales:**

    Volvemos a la raíz del proyecto y ejecutamos el script para craer los 3 dataset necesarios con información de prueba:
    
```bash
    cd ..
    python initial_set.py
```

Esto creará los archivos 
* products.csv
* stores.csv
* prices.csv

3. **Iniciar la API REST:**

Para iniciar la API, entramos en el directorio api y ejecutamos el siguiente comando:

```bash
    cd api
    uvicorn main:app --reload
```

Esto levantará el servidor en modo reload para desarrollo (por defecto en http://127.0.0.1:8000).

FastAPI genera automáticamente documentación interactiva. Puedes acceder a ella en:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

4. **Cargar los datos en la base de datos usando la API:**

```bash
    python load_data.py
```

Este script lee los archivos CSV generados y envía peticiones a la API para agregar productos, establecimientos y precios. Si un precio ya existe y ha cambiado, se actualizará automáticamente.

## Endpoints de la API

**POST** `/products`

Añadir un nuevo producto.

Ejemplo de body:

```json
    {
      "brand": "MarcaA",
      "product_type": "Snack",
      "caloric_value": 250,
      "saturated_fats": 5.5,
      "sugar": 10.0
    }
```

**PUT** `/products/{product_id}`

Actualiza los datos de un producto existente (caloric_value, saturated_fat, sugar)

Ejemplo de body:

```json
    {
      "brand": "MarcaA",
      "product_type": "Snack",
      "caloric_value": 255,
      "saturated_fats": 5.5,
      "sugar": 10.0
    }
```

**POST** `/stores`

Añadir un nuevo establecimiento.

Ejemplo de body:

```json
    {
      "name": "Supermercado1",
      "address": "Calle 123",
      "opening_hours": "08:00-20:00",
      "city": "CiudadX"
    }
```

**POST** `/prices`

Añadir un nuevo precio en un producto para un establecimiento.

Ejemplo de body:

```json
    {
      "product_id": 1,
      "store_id": 1,
      "price": 1.99
    }
```

**GET** `/stores/{store_id}/products`

Devuelve todos los productos asociados a un establecimiento.

## Consideraciones de Negocio

**Validación y Duplicados:**

Se comprueba que un producto o establecimiento no se agregue más de una vez, utilizando restricciones UNIQUE en la base de datos y validaciones en la API.

**Actualización de Precios:**

El endpoint para precios comprueba si ya existe un registro para la combinación producto/establecimiento. Si el precio ha cambiado, se actualiza el registro; si es el mismo, se informa que no hubo cambios.

**Persistencia de Datos:**

Si se desea reiniciar la base de datos, asegúrate de eliminar los volúmenes persistentes (usando `docker-compose down -v`) o borrar manualmente la carpeta mapeada en el host si estás utilizando un volumen local.


