from fastapi import FastAPI
from Routes.Libro import book
app = FastAPI()

app.include_router(book)