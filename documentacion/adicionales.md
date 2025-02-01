

# Componentes adicionales




## NGINX

Este mini servidor web sirve para varios cometidos:
- Load balancer: repartir el tráfico de entrada entre varios servicios del sistema iguales
- Servidor **SSH**-> posiblemente necesario para servidores HTTPS
- Control Ingress: reparte las peticiones de entrada entre los distintos servicios componentes dek sistema.

## Logs (Auditoría)

Es importante crear un sistema para registrar los eventos internos, ya sean estos normales o anómalos

- logs locales: 
pueden ser muy voluminosos. Consumen parte del hsoting
Exigirían un volumen dedicado para ellos.
- logs remotos


## Monitoreo

Hay servicios externos que monitorean el estado de los servicios internos del sistema.


## Documentación

Se podría crear un repositorio unificado con toda la documentación del proyecto.
Si bien GitHub permite leer los documentos Markdown en directo,
opciones como MkDocs o Hugo pueden mejorar notablemente la experiencia de usuario.