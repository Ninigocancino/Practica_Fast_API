from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID

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

# Esta ruta permite obtener un contacto por su id
@app.get("/contactos/{contacto_id}", response_model=Contacto)
def traer_contacto(contacto_id: UUID):
    for contacto in contactos:
        if contacto.id == contacto_id:
            return contacto
    raise HTTPException(status_code=404,detail="Contacto no encontrado")


# Esta ruta permite agregar un nuevo contacto
@app.post("/Agregar/", response_model=Contacto)
def agregar_contacto(contacto: Contacto):
    contactos.append(contacto)
    return contacto


# Esta ruta permite actualizar un contacto existente
@app.put("/contactos/{contacto_id}", response_model=Contacto)
def actualizar_contacto(contacto_id:UUID, update_contacto: Contacto):
    for index, contacto in enumerate(contactos):
        if contacto.id == contacto_id:
            contactos[index] = update_contacto
            contactos[index].id = contacto_id 
            return contactos[index]
    raise HTTPException(status_code=404, detail="Contacto no encontrado")


