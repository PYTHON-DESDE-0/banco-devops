

# MkDocs

## Instalación

```bash
pip install mkdocs-material
```

## Nuevo proyecto

```bash
mkdocs new .
```

Crea una carpeta `docs` con un archivo demo
y un archivo de configuración llamado `mkdocs.yml`.


## Servidor local

```bash
mkdocs serve
mkdocs serve -a localhost:numero_puerto
```



## Contenedores

### Crear imagen (manual)

```bash
podman build  -t imagen-mkdocs  .
```

### Crear contenedor (manual)

```bash
podman build  -t imagen-mkdocs  .
```


