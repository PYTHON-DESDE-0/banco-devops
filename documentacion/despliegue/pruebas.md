# Despliegue local

## Demo

Para correr las prurbas preliminares
se creó el archivo `docker-compose.yaml`
que ya incluye todas las configuraciones predefinidas 
para el despliegue de los contenedores.


## Compose

Sólo hay que ubicarse con la terminal
en la carpeta del proyecto
y ejecutar el comando `compose`:

```bash
docker compose up
```

Hay que esperar hasta que se complete la puesta en marcha,
la cual puede requerir varios minutos.
Docker descargará las imágenes faltantes de manera automática
y generará las imágenes derivadas
a partir de los archivos `Dockerfile`
cuyas rutas se indica en el archivo `docker-compose.yaml`


## Dockerfile

Los archivos `Dockerfile` son los encargados de configurar
la creación de las imágenes necesarias para los contenedores,
determinando la imagen de base, 
instalando componentes necesarios, 
copiando las rutinas, 
etc.


!!! warning "Imágenes previas"

    En caso de realizar modificaciones en el código fuente,
    es prudente **eliminar las imágenes creadas** automáticamente
    con los archivos `Dockerfile`
    antes de invocar al comando `compose`.
    De otra manera, puede pasar que se sigan usando 
    las versiones antiguas de las imágenes creadas
    y 
    por ello el comportamiento del sistema no cambie nunca.

    
## Conexiones por navegador


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


## Bases de datos

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