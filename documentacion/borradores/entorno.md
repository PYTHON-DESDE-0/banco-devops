
# SQLMODEL + ENTORNO

Apuntes rápidos del test


## Entorno

### Archivo de entorno

Archivo`db.env`:
```
POSTGRES_PASSWORD=123456
POSTGRES_USER=postgres
POSTGRES_DB=test-db
```

### Carga en Bash


Cargar variables de entorno en Bash desde el archivo`db.env`:

```bash
set -o allexport; source db.env; set +o allexport
```



https://www.returngis.net/2023/10/cargar-variables-de-entorno-en-un-script-bash-desde-un-env-con-set-allexport/



## SQLModel

### anfitrion

En caso de usar la rutina de SQLModel desde el equipo anfitrion
el dominio de la base de datos será `localhost`.
```bash
export DOMINIO_POSTGRES=localhost 
```
También se permite usar la IP comodín `0.0.0.0`

De esta forma la petición a la base de datos se hará a una URL
como esta:

```http
postgresql://<user>:<pass>w@localhost:<numero_puerto>/test-db
```


### contenedor

Si la rutina de SQLModel funciona en un contenedor 
integrado dentro del archivo Compose el dominio indicado será 
el *nombre de servicio* del contenedor de la base de datos:


```bash
export DOMINIO_POSTGRES=<servicio_postgres>
```


y la petición a la base de datos se hará a una URL
así:

```http
postgresql://<user>:<pass>w@<servicio_postgres>:<numero_puerto>/test-db
```

El nombre de servicio es elegido por el desarrollador adentro del archivo Compose.


IMPORTANTE:

Docker utiliza el archivo Compose para simular una red privada de contenedores,
en analogía a las redes privadas de computadoras físicas.

En este contexto, 
el "nombre de servicio" se ve como un alias asignado al contenedor
pero es en realida un alias para la IP interna del contenedor
dentro de la red privada clase A.




Resolver problemas de conexión con PostgreSQL: https://dev.to/deni_sugiarto_1a01ad7c3fb/fixing-connection-refused-error-between-pgadmin-and-postgres-in-docker-14ge