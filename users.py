from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User


class User(BaseModel):
    name: str
    surname: str
    age: int
    single: bool
    email: str


users_list = [
            User(name="Diego", surname="Andres", age=35, single=True, email="diegoandres@mail.com"),
            User(name="Susan", surname="Marcela", age=33, single=False, email="susanmarcela@mail.com"),
            User(name="Jose", surname="Oscar", age=37, single=False, email="joseoscar@mail.com"),]


@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Diego", "surname": "Andres",
            "age": 35, "single": True, "email": "diegoandres@mail.com"},
        {"name": "Susan", "surname": "Marcela",
            "age": 33, "single": False, "email": "susanmarcela@mail.com"},
        {"name": "Jose", "surname": "Oscar",
            "age": 37, "single": False, "email": "joseoscar@mail.com"},
    ]


@app.get("/users")
async def users():
    return users_list

# Inicia el server: uvicorn users:app --reload
