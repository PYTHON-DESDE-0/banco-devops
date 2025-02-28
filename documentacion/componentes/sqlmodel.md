# SQLModel

SQLModel es un conector de bases de datos basado en SQLAlchemy e incluye tipado heredado de Pydantic.

Está pensado para facilitar la conexión de bases de datos con los servidores implementados con FastAPI.
(De hecho este conector
fue creado por el mismo creador de FastAPI
).

[Página oficial de SQLModel](https://sqlmodel.tiangolo.com/)


## Instalación

El paquete se instala desde PIP:

```bash
pip install sqlmodel
```

Para poder interaccionar con bases de datos PostgreSQL
se necesita un paquete adicional llamado `psycopg2-binary`:

```bash
pip install psycopg2-binary
```


## Demo 


En la [página oficial de SQLModel](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/) se proporcionan demos
para interaccionar con bases SQLite,
las cuales se basan en archivos locales.

Este es el código:

```py
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

# Nueva tabla como clase
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

# Nuevos registros ("filas" de la tabla) como atributos
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

# ruta al archivo SQLite
sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

# creación del conector
engine = create_engine(
    sqlite_url,     # URL a la base de datos
    echo=True       # log por consola
    )  

SQLModel.metadata.create_all(engine)

# transacción con el archivo
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
```

Este código crea una nueva tabla en la base de datos
llamada `hero`
y le asigna tres filas con los datos indicados:


|**id** |**name**| **secret_name**| **age**|
|:---:|:---|:----|:---:|
|1	|Deadpond	|Dive Wilson	| |
|2	|Spider-Boy	|Pedro Parqueador|	|
|3	|Rusty-Man	|Tommy Sharp	  | 48|


Si la tabla ya existe,
entonces se agregan las tres nuevas filas al final.


## Consultas (*queries*)

### SQLite

SQLite trabaja con archivos locales
con extensión `.db`,
los cuales no incluyen autenticación
ni permiso alguno.
La URL requerida para la consulta se reduce

```http
sqlite:///ruta_archivo
```

Si el archivo no se encuentra en la ruta indicada
entonces este se crea.


### Gestores de bases de datos

La mayoría de los gestores de bases de datos
implementan un servidor para consultar la base de datos.
La URL debe incluir
toda la información necesaria para la conexión,
incluyendo el nombre del driver requerido.

En el caso de tener un servidor PostgreSQL
la petición queda como:

```http
postgresql://usuario:contraseña@dominio:puerto/nombre_database
```

Por ejemplo,
una conexión típica en el equipo local 
y con el puerto predeterminado sería:

```http
postgresql://postgres:123456@localhost:5432/test-db
```

y la URL así conformada se usa para crear el conector:

```py
engine = create_engine(
    postgres_url,       # URL a la base de datos
    echo=True           # log por consola (opcional)
    )
```

!!! info "URL con psycopg2"

    En las peticiones a veces se les indica el uso de `psycopg2`:

    ```http
    postgresql+psycopg2://usuario:contraseña@dominio:puerto/nombre_database
    ```


### Variables de entorno

La rutina de Python 
se adapta para poder configurar la URL.
Los parámetros requeridos:
dominio, puerto, usuario, contraseña, etc.
son pasados con ayuda de variables de entorno
precargadas en la *shell*:

```py
import os

# Lectura de variables de entorno - con valores predefinidos
user     = os.getenv("USUARIO_POSTGRES" , default='postgres')
password = os.getenv("PASSW_POSTGRES"   , default='123456'  )
# ...
```
La función `getenv()` del módulo `os`
es la encargada de leer los valores de las variables pedidas
y puede asignarle un valor predefinido si la variable no existe.

La URL se compone con ayuda de un *f-string*:
```py
# ruta al servidor PostgreSQL
ruta = f"postgresql://{user}:{password}@{dominio}:{puerto}/{database}"
print(f"URL de base de datos: {ruta}")
```

Las variables de entorno implementadas son:

- `PUERTO_POSTGRES`
- `DOMINIO_POSTGRES`
- `USUARIO_POSTGRES`
- `PASSW_POSTGRES`
- `DATABASE_POSTGRES`