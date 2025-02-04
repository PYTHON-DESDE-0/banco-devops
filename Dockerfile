# MATERIAL FOR MKDOCS

# imagen oficial
FROM squidfunk/mkdocs-material:latest

# copia adentro la lista de requisitos 
COPY requirements-mkdocs.txt ./

# instalación de paquetes adicionales
RUN pip install --no-cache-dir -r requirements-mkdocs.txt
RUN pip install --upgrade pip



