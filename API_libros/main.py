from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def traer_ruta():
    return {"message": "Bienvenido a nuestra API de gestión de libros"}