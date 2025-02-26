# Fuente:
# https://sqlmodel.tiangolo.com
from typing import Optional
import os
from sqlmodel import Field, Session, SQLModel, create_engine

# Variables de entorno - con valores predefinidos
key = "PUERTO_POSTGRES" 
puerto = os.getenv(key, default='9000')
key = "USUARIO_POSTGRES" 
user = os.getenv(key, default='postgres')
key = "PASSW_POSTGRES" 
password = os.getenv(key, default='123456')
key = "DATABASE_POSTGRES" 
database = os.getenv(key, default='test-db')

key = "DOMINIO_POSTGRES" 
# dominio = os.getenv(key, default='localhost')
dominio = os.getenv(key, default='0.0.0.0')


ruta = f"postgresql://{user}:{password}@{dominio}:{puerto}/{database}"
print(f"URL de base de datos: {ruta}")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine(
    ruta,
    echo=True,
    pool_pre_ping=True,
    )

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()