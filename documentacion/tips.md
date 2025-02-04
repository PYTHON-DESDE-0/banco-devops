# Tips




## Python

### Imágenes oficiales

Imágenes oficiales de Python disponibles en DockerHub:

[DockerHub - Python Images](https://hub.docker.com/_/python/)


## FastAPI

Basado en el [tutorial oficial](https://fastapi.tiangolo.com/deployment/docker/)


### Proxys
    
Si se usa un proxy como NGINX o Traefik hay que agregar la opción `--proxy-headers` al `CMD` del Dockerfile:


```Dockerfile
# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]
```

https://www.restack.io/p/fastapi-answer-docker-setup


### Comandos en archivo compose

Si se usa el docker-compose, también se puede llamar al comando uvicorn:

```docker-compose
version: '3'

services:
web:
    build: .
    command: sh -c "uvicorn main:app --reload --port=8000 --host=0.0.0.0"
    ports:
    - 8000:8000
```

https://dev.to/rajeshj3/dockerize-fastapi-project-like-a-pro-step-by-step-tutorial-7i8


### Paralelización: 
        
Multiples "workers" (contenedores) en Docker/Kubernetes corriendo `fastapi` o `uvicorn`

https://fastapi.tiangolo.com/deployment/server-workers/?h=dock#deployment-concepts


### Lifespan events

Es código que se ejecuta solamente una vez antes de arrancar el servidor.

Se requiere que el Dockerfile use la instrucción `CMD`
en la forma "exec":
``` Dockerfile
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
```
Yno en la forma "shell":

``` Dockerfile
CMD fastapi run app/main.py --port 80
```


[FastAPI - Lifespan events](https://fastapi.tiangolo.com/advanced/events/)

### Cliente Fastapi vs Uvicorn vs Gunicorn

    ????

    [Ver sobre los servidores de Python](servidores.md)



### Incompatibilidades

**WARNING:** de momento, FastAPI parece **no ser compatible** con Python 3.14

Algunas imágenes base compatibles:

```
python:3.13.1-bookworm

python:3.9
python:3.9.21-alpine3.21
python:3.9.21-slim-bullseye    
python:3.9.21-bullseye      
```


### Conexion con SQL 

### - SQLAlchemy

Uno de los ORMs más conocidos escritos para Python.

[Página oficial de  SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html)

#### - SQLModel 

Del creador de FastAPI, 
SQLModel es un conector de bases de datos
**basado en SQLAlchemy**
e incluye tipado
heredado de Pydantic. 

Está pensado para facilitar la conexión de bases de datos con los servidores implementados con FastAPI.

[SQLModel - Página oficial](https://sqlmodel.tiangolo.com)

[SQLModel - testing](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#fastapi-application)


### Extras:


- [CodevoWeb - Acceso y tokens](https://codevoweb.com/restful-api-with-python-fastapi-access-and-refresh-tokens)

- [CodevoWeb - Emails ](https://codevoweb.com/restful-api-with-python-fastapi-send-html-emails)

- [CodevoWeb - RESTful API con PostgreSQL](https://codevoweb.com/crud-restful-api-server-with-python-fastapi-and-postgresql/)








## FLET




[Fly.io](https://flet.dev/docs/publish/web/dynamic-website/hosting/fly-io/)


### Instalación:

```bash
pip install flet        # minima
pip install flet[all]   # completa
```

### Crear proyecto desde plantilla

Crea una app de un contador:
```py
flet create
```
Incluye archivos de configuracion:

[flet.dev - Create a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)


### Ejecución

Servidor web, puerto random:
```py
flet run --web app.py
```

Servidor, puerto específico:
```py
flet run --web --port 8000 app.py
```

[Flet.dev - Host app as a dynamic website](https://flet.dev/docs/publish/web/dynamic-website/#running-the-app-in-production)



### Self-hosting (servidor dinámico):

- App demo;

- Como hacer un **proxy con NGINX**:
configurar `/etc/nginx/sites-available/*` 


[Flet.dev - Self Hosting](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting)


### Crear sitio estático:

Construir sitio web (descarga Flutter): 

```py
flet build web
flet publish
```
Este crea una subcarpeta `build` con necesarios:

- La carpeta `web` con todos los contenidos del sitio web creado;
- El intérprete de Flutter. 


Puesta en funcionamiento:

```py
python -m http.server --directory build/web
```



[Flet.dev - Publish app to a static website](https://flet.dev/docs/publish/web/static-website)


### Crear apps con Flet

Las instrucciones exactas varían con el sistema operativo destino.

[Flet.dev - Publishing Flet app to multiple platforms](https://flet.dev/docs/publish)


