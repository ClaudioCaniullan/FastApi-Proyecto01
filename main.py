# importar librerias

#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path


# crear una instacia Fastapi
app = FastAPI()

#Models

class Location(BaseModel): 
    city : str
    state: str
    country: str

class Person(BaseModel):

    first_name : str 
    last_name : str
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
    name: Optional[str] = Query(
       None, 
       min_length=1, 
       max_length=50,
       title = "Person Name",
       description = "this is the person name, it's between 1 and 50 character"),
    age : str = Query(
        ...,
        title= "Person Age",
        description= "This is the age, it's required") # parametro obligatorio (aunque en todo query parameter debe ser opcional)
): 
    return {name: age}


# Validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(...,gt= 0) #path parameter obligatorio
):
    return {person_id: "It exists"}


# Validaciones: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id : int = Path(
    ..., 
    title = "Person ID", 
    description = "This is de person ID", 
    gt = 0
    ),
    person: Person = Body(...),
    location : Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results