from fastapi import FastAPI
from pydantic import BaseModel

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