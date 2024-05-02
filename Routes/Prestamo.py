from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Prestamo import prestamoEntity, prestamosEntity
from Models.Prestamo import Prestamo
from starlette.status import HTTP_204_NO_CONTENT
prestamo = APIRouter()
db = conn.investigacionMongo.prestamo

@prestamo.get("/prestamos")
def get_prestamos():
    return prestamosEntity(db.find({},{}))

@prestamo.post("/prestamos")
def post_prestamos(prestamo: Prestamo):
    new_prestamo = dict(prestamo)
    id = db.insert_one(new_prestamo).inserted_id
    return str(id)

@prestamo.get("/prestamos/{titulo}")
def get_prestamo(titulo:str):
    return prestamoEntity(db.find_one({"titulo":titulo},{}))

@prestamo.put("/prestamos/{titulo}")
def update_prestamo(titulo:str, prestamo:Prestamo):
    db.find_one_and_update({"titulo":titulo},{"$set": dict(prestamo)})

@prestamo.delete("/prestamos/{titulo}")
def delete_prestamo(titulo:str):
    db.find_one_and_delete({"titulo":titulo})
    return Response(status_code=HTTP_204_NO_CONTENT)
