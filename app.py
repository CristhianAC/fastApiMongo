from fastapi import FastAPI
from typing import Union
from Routes.Libro import book
app = FastAPI()

app.include_router(book)

@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}