# Tips


## Imagenes Docker

### Distribuciones base:

|Distribución base| Nombre clave| 
|:---|:---:|
|Alpine|`alpine`|
|Debian 8 |`jessie`|
|Debian 9 |`stretch`|
|Debian 10|`buster`|
|Debian 11|`bullseye`|
|Debian 12|`bookworm`|
|Ubuntu 16.04|`xenial`|
|Ubuntu 18.04|`bionic`|
|Ubuntu 20.04|`focal`|
|Ubuntu 22.04|`jammy`|
|Ubuntu 23.10|`mantic`|
|Ubuntu 24.04|`noble`|



Alpine usa el gestor de paquetes `apk`
en tanto que Debian y Ubunto usan `apt`.

Alpine tiene una *shell* en `/bin/sh`.

Todas tienen una *shell* en `/bin/bash`.

https://stackoverflow.com/questions/52083380/in-docker-image-names-what-is-the-difference-between-alpine-jessie-stretch-an

https://medium.com/@faruk13/alpine-slim-bullseye-bookworm-noble-differences-in-docker-images-explained-d9aa6efa23ec

### Versiones "slim":

Las versiones *slim* son versiones "rebajadas" de las imágenes
(documentacion eliminada, archivos extra quitados, etc)
y tienen menos capas. 
Gracias a ello estas versiones ocupan menos espacio en disco cuando están en solitario;
sin embargo pueden ocupar más espacio en total que sus versiones completas cuando comparten disco con otras versiones.


https://medium.com/@faruk13/alpine-slim-bullseye-bookworm-noble-differences-in-docker-images-explained-d9aa6efa23ec


### Componentes en C

La mayoría de las distribuciones Linux,
incluyendo Debian y Ubuntu,
trabajan con `glibc` (GNU C library) y `coreutils`
(GNU coreutils).
Alpine usa en cambio `musl libc` y `Busybox`.
Esto hace que los lenguajes y programas que dependen de C
(por ejemplo, el intérprete oficial de Python) 
funcionen diferente.


### Alpine es problemático para trabajar con Python

- Tiempos de instalación exageradamente largos;
- Imágenes creadas más voluminosas, 
aún eliminando caché interna;
- La mayoria de los desarrolladores de Python
no cumplen las dependencias del programa
con los paquetes del sistema
sino que usan los paquetes de PyPi o Conda Forge.

- Bugs inesperados:
    - `msl` no soporta DNS sobre TCP,
    lo cual puede hacer fallar la configuración de Kubernetes;
    - Pila más chica para los hilos, que pueden hacer crashear a Python;
    - Reserva de memoria dinámica mucho más lenta.


https://pythonspeed.com/articles/alpine-docker-python/



## Python

### Imágenes oficiales

Imágenes oficiales de Python disponibles en DockerHub:

https://hub.docker.com/_/python/


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


### Cliente Fastapi vs Uvicorn vs Gunicorn

    ????

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

https://flet.dev/docs/getting-started/create-flet-app


### Ejecución

Servidor web, puerto random:
```py
flet run --web app.py
```

Servidor, puerto específico:
```py
flet run --web --port 8000 app.py
```

https://flet.dev/docs/publish/web/dynamic-website/#running-the-app-in-production



### Self-hosting (servidor dinámico):

- App demo;

- Como hacer un **proxy con NGINX**:
configurar `/etc/nginx/sites-available/*` 


https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting


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



https://flet.dev/docs/publish/web/static-website








