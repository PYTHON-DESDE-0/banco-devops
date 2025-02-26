# Despliegue local

## Demo

Como primer acercamiento a la integración y despliegue del proyecto
se hizo una carpeta `tests` donde se organizan todos los componentes de ejemplo.

La estructura interna es aproximadamente la siguiente:


```bash title="Demo - estructura"
tests
├── db.env
├── docker-compose.yml
├── fastapi
│   ├── app
│   │   ├── __init__.py
│   │   └── main.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── requirements.txt
├── flet
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── src
│       ├── assets
│       └── main.py
└── sqlmodel
    ├── Dockerfile
    ├── requirements.txt
    └── src
        └── main.py
```

- Para correr las pruebas preliminares en Docker
se creó el archivo `docker-compose.yml`,
el cual se encuentra en la carpeta `tests`.
Este archivo ya incluye todas las configuraciones predefinidas 
para el despliegue de los contenedores.

- El archivo `db.env` es el encargado de guardar
los valores de configuración.

- Cada framework o componente de Python utilizado
tiene su propia carpeta interna, incluyendo:
    - su rutina de demo `main.py`;
    - su archivo de dependencias `requirements.txt`;
    - su archivo `Dockerfile` para que Docker pueda crear las imágenes necesarias.

    También es posible desplegar los componentes del demo mediante entornos virtuales usando múltiples *shells*,
    aunque este método es el más engorroso.




## Funcionamiento


### Conexiones por navegador


Una vez completada la puesta en marcha,
se abre el navegador y se prueba ingresar a la ruta local 
(`localhost` o `127.0.0.1`)
agregando los números de puerto especificados.



### Backend

En el caso del backend se eligió el puerto **9001**.
Los demos se ven con las siguientes URLs:


```http
http://localhost:9001/
http://localhost:9001/items/25
```
El resultado es un objeto JSON (un "diccionario" de Python)

La documentación generada por FastAPI se consulta en las rutas:

```http
http://localhost:9001/docs
http://localhost:9001/redocs
```


### Frontend

Para el frontend se eligió el puerto **9002**:
```http
http://localhost:9002/
```
El demo es un contador sencillo
que se incrementa
al hacer click sobre el botón.

### Documentación (local)


La documentación se consulta en el puerto **9003**:
```http
http://localhost:9003/
```

dando lugar a la presente documentación.
Los archivos de texto y de configuración están afuera del directorio del test,
porque son relevantes para todo el proyecto.

### Bases de datos

De momento, la única base de datos utiliza el puerto **9000**.
Se usa un cliente para base de datos
y se crea una conexión para base de datos con los siguientes parámetros:

|variable| valor|
|---|---|
|nombre de driver| PostgreSQL|
|puerto| `9000`|
|usuario| `postgres` |
|contraseña|`123456`|
|nombre database|`test-db`|

El cliente debería ser capaz de conectarse y mostrar las bases de datos internas `postgres` (se crea por default) y `test-db`.


### Cliente de base de datos

Se implementó un cliente que hace una única petición a la base de datos
y se detiene.
La petición consiste en crear una tabla llamada `hero` y agregarle tres filas de datos.
Si la tabla ya existe entonces se repiten las filas de datos.


