from fastapi import FastAPI
from typing import Union
from Routes.Libro import book
from Routes.Autorea import autorea
from Routes.Copia import copia
from Routes.Prestamo import prestamo
from Routes.Usuario import user
from Routes.Edicion import edicion
from Routes.Autor import author
from Routes.Querys import query
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(query)
app.include_router(book)

app.include_router(autorea)
app.include_router(copia)
app.include_router(prestamo)
app.include_router(user)
app.include_router(edicion)
app.include_router(author)
# Configuración para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Comodín * para permitir acceso desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello Guys, this is a FastAPI project for DataBase connection with MongoDB."}