# SQLModel


## Backend vs demo

SQLModel trabaja como parte del backend,
por ello será integrado
junto a las rutinas de FastAPI
y por tanto compartirá contenedor con él.


Como contrapartida,
en el caso del demo
SQLModel se instala en solitario.
Esto es así porque en la rutina de demo
sólo se desea probar la conectividad de la rutina
entre contenedores.


## Compose









## Puertos

Este contenedor no expone ningún puerto.
S


## Variables de entorno

El contenedor necesita los valores de ciertas variables de entorno
para poder crear la URL necesaria para consultar a la base de datos.

Las variables de entorno se parten en dos grupos:

- Los datos de sesión (usuario, contraseñas) se guardan en un archivo `.env` que es especificado desde el archivo Compose.
    Variables incluidas:

    - `USUARIO_POSTGRES`
    - `PASSW_POSTGRES`
    - `DATABASE_POSTGRES`

- Los parámetros de la IP y el puerto de conexión
se indican en el archivo Compose directamente:

    - `PUERTO_POSTGRES`
    - `DOMINIO_POSTGRES`
