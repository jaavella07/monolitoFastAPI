from typing import Annotated # dependencia para el uso de la base de datos por medio de SQLModel

from fastapi import FastAPI
from fastapi import Depends
from sqlmodel import Session,create_engine
from sqlmodel import  SQLModel

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    
    
#Obtener la sesion
def get_session():
    with Session(engine) as session:
        yield session# Retorna la sesion


SessionDep = Annotated[Session, Depends(get_session)] # Dependencia para usar en las rutas