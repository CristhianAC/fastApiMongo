from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Libro import libroEntity, librosEntity
from Models.libro import libro
from starlette.status import HTTP_204_NO_CONTENT
book = APIRouter()
db = conn.investigacionMongo.libro


@book.get("/libros", response_model=libro)
def get_books():
    return librosEntity(db.find({},{}))
@book.post("/libros", response_model=libro)
def post_books(libro: libro):
    new_libro = dict(libro)
    id = db.insert_one(new_libro).inserted_id
    return str(id)

@book.get("/libros/{titulo}", response_model=libro)
def get_book(titulo:str):
    
    return libroEntity(db.find_one({"titulo":titulo},{}))
@book.put("/libros/{titulo}", response_model=libro)
def update_book(titulo:str, libro:libro):
    db.find_one_and_update({"titulo":titulo},{"$set": dict(libro)})
@book.delete("/libros/{titulo}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(titulo:str):
    db.find_one_and_delete({"titulo":titulo})
    return Response(status_code=HTTP_204_NO_CONTENT)