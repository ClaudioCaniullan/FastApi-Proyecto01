# correr proyecto en consola: uvicorn main:app --reload
# visitar documentacion de la API: http://localhost:8000/docs#/

# importar librerias

#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path


# crear una instacia Fastapi
app = FastAPI()

#Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel): 
    city : str
    state: str
    country: str

class Person(BaseModel):

    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50,
        example = "Claudio"
        )
    last_name : str = Field(
        ...,
        min_length=1,
        max_length=50,
        example = "Caniullan"
        )
    age : int = Field(
        ...,
        gt=0,
        le=115,
        example = 38
    )
    hair_color : Optional[HairColor] = Field(default=None, example= "black")
    is_married : Optional[bool] = Field(default=None, example = False)
    
    # forma 2: valores por defecto
    # class Config: 
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "Garcia Martoni",
    #             "age": 21,
    #             "hair_color": "blonde",
    #             "is_married": False
    #         }

    #     }


# crear path operations
@app.get("/")
def Home():
    return {"Hello": "world"}


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
       description = "this is the person name, it's between 1 and 50 character",
       example = "Maria"),
       
    age : str = Query(
        ...,
        title= "Person Age",
        description= "This is the age, it's required",
        example = 25) # parametro obligatorio (aunque en todo query parameter debe ser opcional)
        
): 
    return {name: age}


# Validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(
    ...,
    gt= 0,
    example= 123
    ) #path parameter obligatorio
):
    return {person_id: "It exists"}


# Validaciones: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id : int = Path(
    ..., 
    title = "Person ID", 
    description = "This is de person ID", 
    gt = 0,
    example=123
    ),
    person: Person = Body(...),
    #location : Location = Body(...)
):
    #results = person.dict()
    #results.update(location.dict())
    return person
