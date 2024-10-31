from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#Lista que guardará las recestas de la API
recetas = []

class Recetas(BaseModel):
    nombre_receta: str
    pais_origen: str
    localidad: str
    cultura: str
    idioma_redaccion: str
    ingredientes: str
    anio_origen: str

#Ruta de verificación
@app.get("/")
def verificacion():
    return {"mensaje": "La API esta en línea y lista para mostrar y recibir Recetas"}

#Ruta para traer las recetas
@app.get("/trear_recetas/", response_model=List[Recetas])
def trear_recestas():
    return recetas

#Ruta para agregar datos
@app.post("/agregar/", response_model=Recetas)
def agregar(receta: Recetas):
    recetas.append(receta)
    return receta