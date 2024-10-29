from fastapi import FastAPI

app = FastAPI()

#Ruta de verificación
@app.get("/")
def verificacion():
    return {"mensaje": "La API esta en línea"}

#Ruta para traer las recestas
@app.get("/trear_recetas/")
def trear_recestas():
    return {"Mensaje" : "Estas son todas las recetas"}

#Ruta para agregar datos
@app.post("/agregar/")
def agregar():
    return {"Mensaje" : "Agrega datos"}