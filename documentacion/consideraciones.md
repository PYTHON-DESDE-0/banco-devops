

# Consideraciones preliminares

## Despliegue (*deploy*)

### Modo manual

El despliegue se puede realizar de manera manual (database en un servidor, backend en otro, etc.) aprovechando servicios online dedicados.

### Gestores de contenedores - Docker y Podman

Se piensa en el posible despliegue del sistema completo
tanto en servidores como en equipos de desarrollo
con la ayuda de gestores de contenedores,
donde el más popular es Docker. 
La alternativa inmediata es Podman, 
el cual es altamente compatible con las imágenes de Docker 
y tiene una sintaxis casi idéntica.

El despliegue completo se configura con bastante facilidad con los archivos `compose`.
los cuales permiten también hacer contenedores paralelos para un mejor reparto de carga de CPU,
lo cual da cierto margen de escalabilidad.

### Orquestadores de contenedores - Kubernetes

Es posible pensar a futuro en el despliegue con orquestadores de contenedores como Kubernetes con ayuda de sus *manifiestos*.
Sin embargo, debe señalarse que:

- Kubernetes es considerado como sobreingeniería para sistemas pequeños y medianos: 
no se justifica para varias miles de peticiones por segundo.
- Kubernetes y sus implementaciones para uso en PC (K3S, Minikube, KinD) son bastante más exigentes en recursos de base que Docker o Podman. 
- Los *manifiestos* de Kubernetes también tienen sus propias reglas y complejidades.

## Arquitectura de servicios

Aún no establecida de manera definitiva.
En principio serían tres servicios monolíticos:

- Un servicio de frontend;
- Un servicio de backend;
- Un servicio de SQL;

La regla básica de asignación sería: un servicio - un contenedor.

**PENDIENTE**
Sería interesante 
fragmentar los bloques predefinidos en microservicios
y
poder acomodarlos con topologías como:

- Paquete por capa;
- Paquete por prestación;
- Arquitectura de cebolla;
- Arquitectura hexagonal.




## Componentes



### Frontend - FLET

Flet es un framework apto tanto para crear
tanto apps multiplataforma
(Android, IOS, Windows, Linux) 
como también páginas web 
tanto estáticas como dinámicas.
Es *fork* del popular framework **Flutter** 
y está adaptado al lenguaje Python.


### Backend - FastAPI (test)

FastAPI es un potente framework para crear servidores backend
basado en **Flask**.
Trae integrados los servidores Uvicorn y Guvicorn, 
los cuales ya traen mecanismos integrados para la gestión paralela 
de las peticiones remotas.
Se escribe en Python.


### SQL - PostgreSQL

PostgreSQL es uno de los gestores de bases de datos
más populares y potentes
Es de código abierto y destaca el manejo de bases de datos grandes. 
Hay múltiples servicios online que ofrecen su despliegue.




