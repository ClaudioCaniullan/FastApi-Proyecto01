# importar librerias
from fastapi import FastAPI

# crear una instacia Fastapi
app = FastAPI()

# crear path operations
@app.get("/")
def Home():
    return {"Hello": "world"}

# correr proyecto en consola: uvicorn main:app --reload