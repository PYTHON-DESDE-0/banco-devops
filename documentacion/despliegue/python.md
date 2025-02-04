


# Python


## Imágenes de Python

El lenguaje Python dispone de una 
[gran cantidad de imágenes disponibles](https://hub.docker.com/_/python/) listas para su uso.

La versión de Python más reciente disponible es la 3.14
.


### Imágenes estándar


Las imágenes de Python estándar están basadas en Debian.
Estas imágenes son las más compatibles
para trabajar con todo tipo de programas.
Pesan alrededor de 1GB.


### Alpine es problemático para trabajar con Python

Las imágenes basadas en Alpine
tienen varias desventajas
al correr programas escritos en Python:

- Tiempos de instalación exageradamente largos;
- Imágenes creadas más voluminosas, 
aún eliminando caché interna;
- La mayoria de los desarrolladores de Python
no cumplen las dependencias del programa
con los paquetes del sistema
sino que usan los paquetes de PyPi o Conda Forge.

- Bugs inesperados:
    - `msl` no soporta DNS sobre TCP,
    lo cual puede hacer fallar la configuración de Kubernetes;
    - Pila más chica para los hilos, que pueden hacer crashear a Python;
    - Reserva de memoria dinámica mucho más lenta.

Por este motivo,
se prefiere evitar usar las imágenes basadas en Alpine
para los programas escritos en Python. 

### Versiones `slim`

Las imágenes de Python basadas en Debian tienen sus versiones estándar y sus contrapartes *slim*.
De éstas, las imágenes estándar pesan alrededor de 1GB 
en tanto que sus versiones *slim* pesan apenas poco más de 100MB.

Sin embargo, se advierte que las imágenes *slim* pueden traer conflictos al intentar instalar ciertos paquetes debido a la falta de algunos componentes del sistema.


### Windows Server Core


Estas imágenes están basadas en Windows Server.
Están pensadas para su uso para programas que requieran correr .NET u otros componentes exclusivos de Windows.



## Referencias


[Python Speed - Using Alpine can make Python Docker builds 50× slower](https://pythonspeed.com/articles/alpine-docker-python/)