from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
    