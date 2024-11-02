from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid, UUID

app = FastAPI()

#Esta lista guarda los contactos
contactos = []

#Esta es la estructura de datos para los contactos
class Contacto(BaseModel):
    id: UUID
    nombre: str
    email: str
    telefono: str


# Esta ruta verifica que la API este funcionando
@app.get("/")
def leer_ruta():
    return {"Mensaje" : "La API de contancto esta inciada"}


# Esta ruta muestra todos los contactos
@app.get("/contactos/", response_model=List[Contacto])
def traer_contactos():
    return  contactos

# Esta ruta permite agregar un nuevo contacto
@app.post("/Agregar/", response_model=Contacto)
def agregar_contacto(contacto: Contacto):
    contactos.append(contacto)
    return contacto



