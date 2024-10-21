from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def traer_ruta():
    return {"message": "Bienvenido a nuestra API de gestión de libros"}

#Modelo de datos 
class Libro(BaseModel):
    id:int
    title: str
    author: str
    description: str = None
    year: int
    available: bool = True 

libros = []

#Ruta para agregar un libro al API
@app.post("/books", response_model=Libro)
def agregar_libro(libro: Libro):
    for libro_existente in libros:
        if libro_existente.id == libro.id:
            raise HTTPException(status_code=400, detail="El ID del libro ya existe")
    libros.append(libro)
    return libro
    

#Ruta para obtener todos los libros
@app.get("/libros", response_model=List[Libro])
def traer_libros():
    return libros

#Ruta para obtener un libro especifico por su ID
@app.get("/libros/{libro_id}", response_model=Libro)
def traer_libro(libro_id: int):
    for libro in libros:
        if libro.id == libro_id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")