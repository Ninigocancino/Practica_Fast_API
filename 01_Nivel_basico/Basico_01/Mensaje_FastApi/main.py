from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def mostrar_mensaje():
    return{"Mensaje":"Este es un proyecto básico para aprender FastAPI"}