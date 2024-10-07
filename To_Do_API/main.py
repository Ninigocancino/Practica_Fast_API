from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tarea(BaseModel):
    id : int
    title : str
    description : str = None
    completed : bool = False

tareas = []

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

@app.get("/")
def ruta_raiz():
    return { "Entrando": "Bienvenido a To Do List"}



#Obtener todas las tareas

@app.get("/tareas",response_model=List[Tarea])
def traer_tareas():
    return tareas