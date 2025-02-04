
# Imagenes de Docker


En esta sección se discute qué posibles imágenes 
pueden ser usados para el proyecto
y
se definen algunos criterios para la elección de las mismas. 

Algunos criterios preliminares:

- Se busca en lo posible usar imágenes prearmadas oficiales de los frameworks y componentes elegidos;
- Si se necesita instalar los frameworks entonces se eligen las imágenes oficiales del lenguaje usado;
- Se deja como última opción el uso de las imágenes base de los sistemas operativos.

También se enumeran algunas características deseables:

- Bajo espacio en disco;
- Reutilización para varios componentes;
- Buena *performance* corriendo programas en Python cuando corresponda.


## Distribuciones base

Las imágenes de Docker se basan habitualmente
en distribuciones GNU/Linux,
las cuales son decapadas de los componentes innecesarios 
(interfases gráficas, aplicaciones de usuario, etc)
y son empaquetadas.
Estas son las distribuciones más habituales 
para crear imágenes en el presente:

|Distribución base| Nombre clave| 
|:---|:---:|
|Alpine|`alpine`|
||
|Debian 8 |`jessie`|
|Debian 9 |`stretch`|
|Debian 10|`buster`|
|Debian 11|`bullseye`|
|Debian 12|`bookworm`|
||
|Ubuntu 16.04|`xenial`|
|Ubuntu 18.04|`bionic`|
|Ubuntu 20.04|`focal`|
|Ubuntu 22.04|`jammy`|
|Ubuntu 23.10|`mantic`|
|Ubuntu 24.04|`noble`|
||
|Windows Server|`windowsservercore`|


En general, es deseable usar en lo posible
las imágenes basadas en las versiones más recientes
de la distribución base elegida.


## Shells y gestores de paquetes 

Alpine usa el gestor de paquetes `apk`
en tanto que Debian y Ubunto usan `apt`.

Alpine tiene una *shell* interna en `/bin/sh`.
Todas tienen una *shell* interna en `/bin/bash`.


Esto es importante en caso que se necesite instalar componentes y bibiotecas para el sistema operativo.



## Versiones *slim*

Las versiones *slim* son versiones "rebajadas" de las imágenes
(documentacion eliminada, archivos extra quitados, etc)
y tienen menos capas (*layers*) internas. 
Gracias a ello estas versiones ocupan
mucho menos espacio en disco 
cuando están en solitario;
sin embargo pueden ocupar más espacio en total
que sus versiones completas
cuando comparten disco con otras imágenes.


<!-- 
Por ejemplo, las imágenes base de Python
basada en Debian pesan alrededor de 1GB; 
sin embargo, sus versiones *slim* pesan apenas poco más de 100MB.

Por otra parte, 
las imágenes de Python basadas en Alpine pesan alrededor de 50MB;
sin embargo éstas últimas tienen varias contrapartidas quese verán a continuación. 
-->


## Componentes en C

La mayoría de las distribuciones Linux,
incluyendo Debian y Ubuntu,
trabajan con `glibc` (GNU C library) y `coreutils`
(GNU coreutils).
En cambio, Alpine usa `musl libc` y `Busybox`.
Esto hace que los lenguajes y programas que dependen de 
componentes escritos en C
(por ejemplo, el intérprete oficial de Python) 
funcionen diferente.





## Referencias

[Medium.com - Alpine, Slim, Bullseye, Bookworm, Noble — Differences in Docker Images Explained](https://medium.com/@faruk13/alpine-slim-bullseye-bookworm-noble-differences-in-docker-images-explained-d9aa6efa23ec)



[StackOverflow - In Docker image names what is the difference between Alpine, Jessie, Stretch, and Buster?](https://stackoverflow.com/questions/52083380/in-docker-image-names-what-is-the-difference-between-alpine-jessie-stretch-an)