# Despliegue con contenedores


## Introducción a los contenedores

Los contenedores son una herramienta
para el despliegue de proyectos
que permite una gran versatilidad.

Uno de los puntos fuertes del uso de contenedores
es la posibilidad de utilizar
múltiples versiones de un mismo software
al mismo tiempo,
permitiendo un alto grado de control 
por parte de los desarrolladores
respecto a los componentes de software utilizados.


Los contenedores trabajan
en base a direcciones IPs y puertos para relacionarse unos con otros.

## Gestores y Orquestadores

Tanto los programas gestores de contenedores
como los programas orquestadores de contenedores
permiten crear, configurar y controlar los contenedores.
Sin embargo están pensados con distintos requisitos.

Los gestores de contenedores
tienen por objetivo el despliegue
en un único servidor,
el cual puede ser un equipo local
o puede ser también un servidor en internet. 
El gestor de contenedores dominante es Docker,
la cual es privativa y tiene la marca registrada.
Una alternativa muy similar a Docker respecto al uso,
sintaxis y recursos es Podman,
el cual es soportado por RedHat
y trata de cumplir con los requisitos
de la Open Container Initiative (*OCI*). 

Por otra parte,
los orquestadores tienen por propósito el despliegue en redes de servidores,
los cuales son coordinados por el programa orquestador
para crear y sostener los contenedores
,implementando mecanismos de confiabilidad y redundancia
para asegurar una alta disponibilidad de los servicios.
El orquestador más popular es Kubernetes,
también llamado K8S,
el cual fue desarrollado por Google. 
Éste tiene varias alternativas reducidas como KinD, K3S, Minikube, etc. 
Docker Compose y sus clones
son considerados también como orquestadores
pero con prestaciones reducidas,
los cuales facilitan el despliegue
por parte de los gestores de contenedores. 



## Elementos

El gestor de contenedores
maneja varios tipos de elementos complementarios
para poder realizar el despliegue de los proyectos. 


### Contenedores (`containers`)

Los contenedores son máquinas virtuales hiper simplificadas,
las cuales son desplegadas en un entorno controlado,
aislados del sistema anfitrión. 


### Imágenes (`images`)

Las imágenes de los contenedores son los equivalentes a las imágenes de instalación de los sistemas operativos.
Son los "sistemas operativos" de los contenedores sobre los cuales se instalan los programas.

### Capas (`layers`)

Los archivos de las imágenes
se distribuyen en capas (*layers*),
las cuales pueden ser reutilizadas por mútiples imágenes
con el fin de reducir el espacio total ocupado en el almacenamiento.
Las capas son controladas por el programa gestor/orquestador.

### Volumenes (`volumes`)

Los volumenes son almacenamientos persistentes
a los que los contenedores pueden acceder.
Son equivalentes a los almacenamientos extraíbles de los equipos físicos

Los volumenes pueden ser rutas específicas del sistema anfitrión
a la cual el gestor tiene acceso
o pueden ser elementos abstractos
creados en una carpeta especial por el programa gestor.

### Redes (`networks`)

Las redes son elementos auxiliares
que se usan para conectar a los contenedores entre sí
en aquellos casos que sea necesario.

Cada *network* equivale 
a una red privada
donde a cada contenedor con acceso
tiene una IP privada que lo diferencia del resto. 


!!! info "IPs clase A" 

    Las redes creadas típicamente son clase A
    de ahí que la IP interna de cada contenedor
    tenga la forma 10.x.x.x 



## Opciones y herramientas

Hay varias opciones y herramientas
proporcionadas por los gestores de contenedores
para trabajar con los contenedores.


### Comandos 

Los comandos son la forma más engorrosa de trabajar con contenedores y sus auxiliares,
sin embargo son útiles para diagnósticos,
correcciones sobre la marcha, 
etc.

Los comandos se escriben desde la terminal.

### Dockerfile

Los archivos `Dockerfile` son los archivos encargados de configurar
la creación de las imágenes necesarias para los contenedores,
determinando la imagen de base, 
instalando componentes necesarios, 
copiando las rutinas, 
etc.

Estos archivos pueden ser ejecutados por comandos (`docker build`)
o ser invocados indirectamente 
desde el archivo
`docker-compose.yml`.

En los archivos `Dockerfile`
siempre se asume que existe una imagen previa,
con la cual se construye una nueva con más componentes.

### Docker Compose


Los archivos `docker-compose.yml` 
son archivos que facilitan configurar
todos los parámetros de los contenedores del proyecto
y sus elementos auxiliares en un archivo YAML,
permitiendo el despliegue (*deploy*)
con un sólo comando en la terminal.

Las secciones habituales de este archivo son:

- `services`: 
los servicios son los contenedores del proyecto,
cada uno con sus parámetros,
un nombre de 'servicio' y su IP interna;
- `volumes`:
volumenes del proyecto. y sus opciones
- `networks`:
redes usadas en el proyecto y sus configuraciones.


Formato típico:
``` yaml
services:

  servicio-1:
    image: imagen-1


  servicio-1:
    image: imagen-2


volumes:
  volumen-1:
  volumen-2:
    external: true


networks:
  red_1:
```



!!! info "Nombre de servicio vs nombre de contenedor" 

    En el archivo Compose el nombre de servicio
    toma la apariencia de un alias para 
    el nombre de contenedor.
    Sin embargo, son dos atributos distintos:

    - El nombre del servicio equivale a un *nombre de dominio*
    con el cual puede ser consultado
    por otros servicios del proyecto
    mediante el protocolo IP.  

    - El nombre del contenedor sirve para ser accedido desde el gestor de contenedores mediante la *shell*.
    Puede ser definido por el usuario
    mediante el atributo `container_name`.

    Ejemplo:

    ``` yaml
    services:

        database:                       # nombre de servicio
            image: postgres:latest
            container_name: postgres-db # nombre de contenedor
    ```


## Compose

Para realizar el despliegue automático en Docker
sólo hay que ubicarse con la terminal
en la carpeta 
donde se ubica el archivo `docker-compose.yml`
y ejecutar el comando `compose`:

```bash
docker compose up
```

Hay que esperar hasta que se complete la puesta en marcha,
la cual puede requerir varios minutos
la primera vez;
mientras tanto,
la *shell* irá mostrando los reportes del proceso.
Docker descargará las imágenes faltantes de manera automática
y generará las imágenes derivadas
a partir de los archivos `Dockerfile`
cuyas rutas se indica en el archivo `docker-compose.yaml`.
El funcionamiento se interrumpe con ++ctrl+c++.


El despliegue independiente se consigue agregando la opción `-d`:

```bash
docker compose up -d
```

y para el cierre y eliminación del despliegue actual se usa:
```bash
docker compose down 
```

!!! warning "Imágenes previas"

    En caso de realizar modificaciones en el código fuente,
    es prudente **eliminar las imágenes creadas** automáticamente
    con los archivos `Dockerfile`
    antes de invocar al comando `compose`.
    De otra manera, puede pasar que se sigan usando 
    las versiones antiguas de las imágenes creadas
    y 
    por ello el comportamiento del sistema no cambie nunca.

    