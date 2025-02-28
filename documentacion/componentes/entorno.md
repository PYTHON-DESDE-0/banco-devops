# Variables de entorno

Las variables de entorno son variables que maneja la terminal
(la *shell*)
para el proceso que corre 
y que comparte con los procesos que invoca.


## Variables en Bash

En este artículo se asume el uso de la terminal Bash
para todos los comandos.

### Asignación manual

La creación de estas variables se realiza con el comando `export`:

```bash
export MI_VARIABLE=25
```
La costumbre es escribir los nombres
de las variables de entorno
en mayúsculas.

Los valores son modificables *a posteriori*
con una simple asignación:

```bash
MI_VARIABLE="hola, que tal"
```

### Consulta

Los valores se consultan con el comando `echo`:

```bash 
echo $MI_VARIABLE
```

Si la variable es inexistente
entonces no se muestra nada.


## Archivos de entorno

Las variables de entorno
se suelen guardar
en archivos con el nombre `.env` (oculto)
o en archivos con extensión `.env`.


### Sintaxis

Las variables se guardan en formato texto como asignaciones.

Ejemplo: un archivo llamado `variables.env`:

```
USER=soy_yo
PASSWORD=123456
```

!!! warning "gitignore"

    Es importante agregar los archivos `.env`
    al archivo `.gitignore` 
    para prevenir el guardado de los valores
    de las variables de entorno sensibles
    en el repositorio de Git.

    ```
    .env
    *.env
    ```

### Lectura

La carga de los valores se hace con los siguientes comandos:

```bash
set -o allexport        
source variables.env       
set +o allexport    
```
o:

```bash
set -o allexport; source variables.env; set +o allexport    
```

Explicación:

- `set -o allexport` habilita que los subprocesos de la actual *shell* 
puedan recibir los valores de las variables;
- `source variables.env` lee las variables y sus desde el archivo;
- `set +o allexport` "desacopla" a los subprocesos
ante posibles cambios de valor de estas variables.


## Referencias

[Returngis.net - Cargar variables de entorno en un script Bash](https://www.returngis.net/2023/10/cargar-variables-de-entorno-en-un-script-bash-desde-un-env-con-set-allexport/)