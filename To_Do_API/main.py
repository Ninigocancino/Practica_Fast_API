from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tarea(BaseModel):
    id : int
    title : str
    description : str = None
    completed : bool = False

tareas = []

"""
#Crear tareas

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

"""

#10.-Evitar IDs duplicado (modificación a 'crear tareas)
@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    for tarea_existe in tareas:
        if tarea_existe.id == tarea.id:
            raise HTTPException(status_code=400,deatil="El ID de la tarea ya existe")
    tareas.append(tarea)
    return tarea




@app.get("/")
def ruta_raiz():
    return { "Entrando": "Bienvenido a To Do List"}



#2.-Obtener todas las tareas

@app.get("/tareas",response_model=List[Tarea])
def traer_tareas():
    return tareas

#Obtener una tarea especifica

@app.get("/tareas/{tarea_id}", response_model=Tarea)
def traer_tarea(tarea_id:int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404,detail="Tarea no encontrada")


#Actualizar tarea
@app.put("/tareas/{tarea_id}", response_model=Tarea)
def update_tarea(tarea_id: int, update_tarea: Tarea):
    for index, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            tareas[index] = update_tarea
            return update_tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


#Eliminar tareas
@app.delete("/tarea/{trea_id}", response_model=Tarea)
def eliminar_tarea(tarea_id:int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tareas.remove(tarea)
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

