from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def leer_ruta():
    return {"mensaje 1" : "Haola Fast API"}