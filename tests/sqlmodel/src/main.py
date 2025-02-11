# Fuente:
# https://sqlmodel.tiangolo.com
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


import os


# puerto = os.environ( "PUERTO"  )
# key = "PUERTO" 
# print(f"SQLMODEL - TEST")
# print()
key = "PUERTO_POSTGRES" 
puerto = os.getenv(key, default='9000')
# puerto = str(puerto)
key = "USUARIO_POSTGRES" 
user = os.getenv(key, default='postgres')
# user = str(user)
key = "PASSW_POSTGRES" 
password = os.getenv(key, default='123456')
# password = str(password)
key = "DATABASE_POSTGRES" 
database = os.getenv(key, default='test-db')
# database = str(database) 
# print(f"PUERTO_POSTGRES: {puerto}")
# print()



class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

# engine = create_engine("postgresql://postgres:123456@localhost:9000/test-db")
# engine = create_engine(
#     "postgresql+psycopg2://postgres:123456@localhost:9000/test-db",
#     echo=True
#     )

# ruta = f"postgresql+psycopg2://{user}:{password}@localhost:{puerto}/{database}"
ruta = f"postgresql://{user}:{password}@localhost:{puerto}/{database}"
print(f"Ruta db: {ruta}")
print(type(ruta))

engine = create_engine(
    ruta,
    echo=True
    )

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()