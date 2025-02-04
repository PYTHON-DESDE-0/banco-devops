# MATERIAL FOR MKDOCS

# imagen oficial
FROM squidfunk/mkdocs-material:latest

# copia adentro la lista de requisitos 
COPY requirements-mkdocs.txt ./

# Entorno virtual (previene errores por permisos de root en Podman)
RUN py -m venv .venv
RUN source .venv/bin/activate

# instalación de paquetes adicionales
RUN pip install --no-cache-dir -r requirements-mkdocs.txt \
    & pip install --upgrade pip



