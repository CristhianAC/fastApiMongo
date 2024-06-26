from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Libro import libroEntity, librosEntity
from Models.libro import libro

from starlette.status import HTTP_204_NO_CONTENT
book = APIRouter()
db = conn.investigacionMongo.libro
dbA = conn.investigacionMongo.autorea
dbE = conn.investigacionMongo.edicion

@book.get("/libros")
def get_books():
    return librosEntity(db.find({},{}))

@book.post("/libros")
def post_books(libro: libro):
    new_libro = dict(libro)
    id = db.insert_one(new_libro).inserted_id
    return str(id)

@book.get("/libros/{titulo}")
def get_book(titulo:str):
    return libroEntity(db.find_one({"titulo":titulo},{}))

@book.put("/libros/{titulo}")
def update_book(titulo:str, libro:libro):
    db.find_one_and_update({"titulo":titulo},{"$set": dict(libro)})
    dbA.update_many({"tituloLibro":titulo},{"$set": {"tituloLibro":libro.titulo}})
    dbE.update_many({"titulo":titulo},{"$set": {"titulo":libro.titulo}})
    
@book.delete("/libros/{titulo}")
def delete_book(titulo:str):
    dbE.delete_many({"titulo":titulo})
    dbA.delete_many({"tituloLibro":titulo})
    db.find_one_and_delete({"titulo":titulo})
    return Response(status_code=HTTP_204_NO_CONTENT)