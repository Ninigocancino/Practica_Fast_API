from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def traer_ruta():
    return {"message": "Bienvenido a nuestra API de gestión de libros"}

#Modelo de datos 
class libro(BaseModel):
    id:int
    title: str
    author: str
    description: str = None
    year: int
    available: bool = True 

libros = []