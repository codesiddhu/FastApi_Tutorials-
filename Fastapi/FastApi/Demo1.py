from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return {"message":"hello world"}

@app.get("/greet")
def greet():
    return {"message":"hello Sreedhar"}

# @app.get("/greet/{name}")
# def greet_name(name:str):
#     return {"message":f"hello   {name}"}

@app.get("/greet/{name}")
def greet_name(name:str,age :Optional[int]=None):
    return {"message":f"hello {name}","age":{age}}



class Student(BaseModel):
    name:str
    age:int
    roll:int

@app.post("/create_student")
def create_student(student:Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll_no":student.roll

    }