from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class inventario(BaseModel):
    id : int
    titulo : str
    autor : str
    anio : int
    descripcion : str 
    disponible : bool = True

agregar = []

@app.get("/")
def ruta_raiz():
    return { "status" : "Iniciado"}

@app.post("/agregar")
def ingresar_libro(elemento: inventario):
    agregar.append(elemento)
    return elemento 
