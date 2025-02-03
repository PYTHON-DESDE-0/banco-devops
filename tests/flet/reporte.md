





## Servidores/comandos


## Flet

Da soporte para web.
Es MUY lento

```py
flet run  main.py --web --port 8000
# MUY LENTO
```

```Dockerfile
CMD ["flet", "run", "src/main.py","--web", "--port", "8000"]  
```


## Uvicorn

Cambiar la línea de llamado al intérprete:

```py
# archivo 'main.py'
ft.app(main)
```
por:

```py
# archivo 'main.py'
app = ft.app(main, export_asgi_app=True)
```

Entonces llamar al servidor *uvicorn*:

```py
uvicorn main:app --port 8000    
# BIEN    
uvicorn main:app --port 8000  --host 0.0.0.0
# ???
``` 

En caso de usar contenedores, hacer:
<!-- 
```Dockerfile
CMD ["uvicorn", "main:app", "--port", "8000"]
# MAL - NUNCA MUESTRA LA APP
``` 
-->

```Dockerfile
CMD ["uvicorn", "src.main:app", "--port", "8000", "--host", "0.0.0.0"]
# BIEN !!!
```


Para usar containers,
agregar  `--host 0.0.0.0` 
para que el gestor de contenedores
**permita conexiones desde afuera**.

https://docker-fastapi-projects.readthedocs.io/en/latest/uvicorn.html


## Hypercorn

https://github.com/pgjones/hypercorn/

Requiere instalacion

```bash
pip install hypercorn
```

```py
hypercorn main:app --bind 0.0.0.0:8000
# BIEN
```

```Dockerfile
CMD ["hypercorn", "src.main:app", "--bind", "8000:0.0.0.0"]
# MAL
```