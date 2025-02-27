# PostgreSQL

PostgreSQL, 
también llamado 'Postgres',
es un sistema de administración de bases de datos relacionales
(ORDBMS)
.



## Imágenes de PostgreSQL

Postgres proporciona una lista de [imágenes oficiales](https://hub.docker.com/_/postgres/)
ya preparadas para su uso en contenedores.
Estas están implementadas sobre imágenes tanto de Debian como de Alpine.


## Variables de entorno

Las configuraciones de las imágenes de gestores de bases de datos 
se realizan mediante variables de entorno predefinidas.
Las variables de entorno más importantes de PostgreSQL son las siguientes:


```bash title="PostgreSQL - variables de entorno"
POSTGRES_PASSWORD   # contraseña (OBLIGATORIA)
POSTGRES_USER       # usuario ('postgres' por default)
POSTGRES_DB         # nombre para nueva base de datos
```

Una forma experimental de cargar estos datos desde el archivo Compose 
es bajo el atributo `environment`:

```yaml title="Compose - variables de entorno"
# archivo 'docker-compose.yaml'
services:
  postgres-test:
    image: postgres
    environment:
      POSTGRES_PASSWORD:  "123456"
      POSTGRES_USER:      "postgres"
      POSTGRES_DB:        "test-db"
```

sin embargo los datos sensibles quedan expuestos.
Una opción mejor es usar archivos de configuración `.env`
con el atributo `env_file`:

```yaml title="Compose - variables de entorno en archivo"
# archivo 'docker-compose.yaml'
services:
  postgres-test:
    image: postgres
    env_file: db.env
```

donde el archivo `db.env` trae guardadas las variables y sus valores:

```py title="archivo 'db.env'"
POSTGRES_PASSWORD=123456
POSTGRES_USER=postgres
POSTGRES_DB=test-db
```
Una segunda alternativa es el uso de los ***"secrets"*** de Docker.


<!-- 
!!! danger "Exposicion de datos"

    Los datos de configuración quedan a la vista de cualquiera con este método.
    Opciones alternativas:

     - **archivo `.env`** con las variables de entorno gardadas;
     - ***"secrets"*** de Docker.
 -->


## Puertos

La imagen de PostgreSQL usa el puerto 5432 para las conexiones con los clientes.
Los *sockets* usados por Posgres
son siempre del tipo TCP.

Para hacer el 'mapeo' de puertos
a un puerto distinto
del sistema anfitrión,
desde el archivo Compose se hace:

```yaml
# archivo 'docker-compose.yaml'
services:
  postgres-test:
    image: postgres
    ports:
      - '9000:5432'
```
en este ejemplo se expone el puerto 9000 para que Postgres pueda ser consultado desde el sistema anfitrión.
Los otros contenedores pueden consultar mediante el puerto predefinido.

## Volumenes

Los gestores de contenedores borran toda la data interna
de los contenedores
cada vez que los cierran.
Debido a la naturaleza persistente de las bases de datos,
es indispensable crear *volúmenes* (almacenamientos persistentes) para que el ORM le asigne los datos adentro
y así estos no se pierdan.

Las imágenes de Postgres 
guardan las bases de datos
en la ruta interna
`/var/lib/postgresql/data`.
Esta ruta debe ser asignada a un volumen
para que se resguarde la base de datos correctamente.

En el caso crear los contenedores con archivos *compose*
se crea un volumen en la sección `volumes` y se le asigna la ruta de la imagen dentro de la definición del contenedor:

```yaml
# archivo 'docker-compose.yaml'
services:
  postgres-test:
    image: postgres
    volumes:
      - 'volumen-db:/var/lib/postgresql/data'  # montaje volumen

volumes:   
  volumen-db:       # creación volumen
```

Si se busca que el volumen sea externo, 
es decir que éste debe ser creado
deliberadamente por el desarrollador,
se añade la opción `external` en la definición:

```yaml
# archivo 'docker-compose.yaml'
volumes:   
  volumen-db:       # creación volumen
    external: true  # debe ser preexistente
```

!!! info "Volumenes - Creacion manual"

    Los volúmenes se crean manualmente con Docker mediante la terminal:

    ```bash
    docker volume create  nombre_volumen
    ```

    Y la ubicacíón de su información guardada aparecerá en la ruta del sistema anfitrión indicada por:

    ```bash
    docker volume inspect --format {{.Mountpoint}}  nombre_volumen
    ```
    Rutas habituales:

    === "Windows"

        ```bash
        ???
        ```

    === "GNU/Linux"

        ```bash
        /home/USUARIO/.local/share/containers/storage/volumes/volumen_exterior/_data
        ```



## Referencias

[Docker Hub - Postgres](https://hub.docker.com/_/postgres/)

[DelfStack - Puerto predeterminado de PostgreSQL](https://www.delftstack.com/es/howto/postgres/postgres-default-port/)

[Docker Docs - Volumes](https://docs.docker.com/engine/storage/volumes/)