# importar librerias

#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query


# crear una instacia Fastapi
app = FastAPI()

#Models
class Person(BaseModel):

    first_name = str
    last_name = str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None

# crear path operations
@app.get("/")
def Home():
    return {"Hello": "world"}

# correr proyecto en consola: uvicorn main:app --reload

# Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body()):
    return person 



# Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age : str = Query(...) # parametro obligatorio (aunque en todo query parameter debe ser opcional)
):
    return {name: age}