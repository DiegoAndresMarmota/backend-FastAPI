from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users():
    return "Hi Users!"

# Inicia el server: uvicorn users:app --reload