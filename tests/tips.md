
# Tips

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