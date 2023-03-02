from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    single: bool
    email: str


users_list = [
            User(id=1, name="Diego", surname="Andres", age=35,
                 single=True, email="diegoandres@mail.com"),
            User(id=2, name="Susan", surname="Marcela", age=33,
            single=False, email="susanmarcela@mail.com"),
            User(id=3, name="Jose", surname="Oscar", age=37,
                 single=False, email="joseoscar@mail.com"),
            ]


# @app.get("/usersjson")
# async def usersjson():
#     return [
#         {"name": "Diego", "surname": "Andres",
#             "age": 35, "single": True, "email": "diegoandres@mail.com"},
#         {"name": "Susan", "surname": "Marcela",
#             "age": 33, "single": False, "email": "susanmarcela@mail.com"},
#         {"name": "Jose", "surname": "Oscar",
#             "age": 37, "single": False, "email": "joseoscar@mail.com"},
#     ]

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado una id asociado a ese usuario"}

# Paths


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


@app.post("/user/")
async def user(user: User):
    try:
        if type(search_user(user.id)) == User:
            return {"error": "El usuario ya existe"}
        else:
            users_list.append(user)
            return user
    except:
        return {"error": "No se ha podido agregar un nuevo usuario"}


@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
            if saved_user.id in user.id:
                users_list[index] = user
                found = True

    if not found:
                return {"error": "El usuario no ha sido actualizado"}
    return user




# Inicia el server con: uvicorn users:app --reload
