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

```bash
POSTGRES_PASSWORD   # contraseña (OBLIGATORIA)
POSTGRES_USER       # usuario  
POSTGRES_DB         # nombre para nueva base de datos
```

Una forma experimental de cargar estos datos desde el archivo Compose es la siguiente:

```yaml
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


## Puertos

La imagen de PostgreSQL usa el puerto 5432 para las conexiones con los clientes.
Los *sockets* usados por Posgres
son siempre del tipo TCP.

Para hacer el 'mapeo' de puertos
a un puerto distinto
desde el archivo Compose se hace:

```yaml
# archivo 'docker-compose.yaml'
services:
  postgres-test:
    image: postgres
    ports:
      - '9000:5432'
```
en este ejemplo se expone el puerto 9000 para que Postgres pueda ser consultado.

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



## Referencias

[Docker Hub - Postgres](https://hub.docker.com/_/postgres/)

[DelfStack - Puerto predeterminado de PostgreSQL](https://www.delftstack.com/es/howto/postgres/postgres-default-port/)

[Docker Docs - Volumes](https://docs.docker.com/engine/storage/volumes/)