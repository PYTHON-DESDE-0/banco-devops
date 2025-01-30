

# Banco - DevOps


## Introducción

Este repositorio forma parte
de un proyecto de desarrollo 
de un banco virtual. 

En este repositorio se configura
el despliegue del proyecto del banco
(backend,frontend y database)
pensando en el uso de contenedores.


## Consideraciones de diseño

[**VER AQUI**](documentacion/consideraciones.md)


## Tips

[Apuntes, tips y borradores](documentacion/tips.md) 




## Despliegue (*deploy*)


### Frontend

(NO IMPLEMENTADO)

### Backend


De momento se despliega el demo ubicado en el directorio `fastapi-test`.
Se proporciona un archivo `Dockerfile`
el cual copia el código fuente (subcarpeta `app`) adentro de la futura imagen.

#### Despliegue manual

Se crea la imagen del software:

```bash
cd fastapi-test     
podman build  -t imagen-fastapi  .
```
La imagen creada se llama en este ejemplo `imagen-fastapi`.

Ahora se crea un contenedor con nombre `contenedor-fastapi` y se pone en marcha en el puerto que se elija:

```bash
PUERTO_FASTAPI=8000
docker run  --replace --name contenedor-fastapi  -p$PUERTO_FASTAPI:80  imagen-fastapi
```
#### Despliegue automático

El despliegue automático usa el `docker-compose.yml`

```bash
cd fastapi-test  
export PUERTO_FASTAPI=8000
podman compose up 
```

#### Test

El demo corre en la dirección `localhost` (`127.0.0.1`) con el puerto elegido. Abrir en el navegador:

```http
http://localhost:8000
http://127.0.0.1:8000
```

El demo también deja visitar URIS internas dentro de la ruta `items` dentro de la URL:

```http
http://localhost:32000/items/8
```



### Base SQL

(NO IMPLEMENTADO)

### Sistema completo

(NO IMPLEMENTADO)