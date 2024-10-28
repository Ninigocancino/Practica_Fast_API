from fastapi import FastAPI

app = FastAPI()

# Esta ruta verifica que la API este funcionando
@app.get("/")
def leer_ruta():
    return {"Mensaje" : "La API de contancto esta inciada"}


# Esta ruta muestra todos los contactos
@app.get("/canotactos/")
def traer_contactos():
    return {"Mensaje": "Aquí se mostrará la lista de contactos"}

# Esta ruta permite agregar un nuevo contacto
@app.post("/Agregar/")
def agregar_contacto():
    return {"Mensaje" : "Aquí puedes agregar un contacto"}



