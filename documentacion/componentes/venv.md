

# Entornos virtuales

En Python es habitual crear entornos virtuales,
los cuales son réplicas del intérprete de Python 
creadas normalmente adentro del directorio de cada proyecto.
Cada entorno permite instalar paquetes de Python
de manera independiente al intérprete de Python principal.
Esto ayuda a prevenir conflictos de dependencias
entre los paquetes de distintos proyectos.

## Módulo venv

Un modo habitual de crear un entorno virtual es el módulo **venv**,
que viene integrado al intérprete de Python.


## Creación

**venv** crea un directorio con los archivos de Python adentro:

```bash 
py -m venv .venv
```
La carpeta creada en este caso se llama `venv` y es oculta.

## Activación

La activación del entorno virtual se realiza con el comando `source`.

=== "Bash - Linux"
    
    ```bash 
    source .venv/bin/activate
    ```

=== "Bash - Windows"

    ```bash 
    source .venv/Scripts/activate
    ```

Lo que hace el comando `source`
es alterar la variable de entorno de Python
`PYTHONPATH`,
la cual es una lista de directorios donde se buscan los módulos y paquetes requeridos. 
`source` coloca la ruta del entorno virtual al comienzo de la lista, 
haciendo que el intérprete
del entorno virtual
busque las dependencias en su propio directorio primero.

La instalación de los paquetes y el llamado al intérprete
se realiza de la manera habitual.
<!-- 
```bash
pip install paquete_1 paquete_2     # instalacion - paquete a paquete
pip install -r requirements.txt     # instalacion - desde lista de requisitos
py rutina.py 
``` 
-->

## Desactivación

El entorno virtual se desactiva con el comando `deactivate`:

```bash 
deactivate
```



