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

@prestamo.get("/prestamos/{ISBN}/{numeroCopia}")
def get_prestamo(ISBN:str, numeroCopia:int):
    return prestamoEntity(db.find_one({"ISBN":ISBN, "numeroCopia":numeroCopia},{}))

@prestamo.put("/prestamos/{ISBN}/{numeroCopia}")
def update_prestamo(ISBN:str, numeroCopia:int, prestamo:Prestamo):
    db.find_one_and_update({"ISBN":ISBN, "numeroCopia":numeroCopia},{"$set": dict(prestamo)})

@prestamo.delete("/prestamos/{ISBN}/{numeroCopia}")
def delete_prestamo(ISBN:str,numeroCopia:int):
    db.find_one_and_delete({"ISBN":ISBN, "numeroCopia":numeroCopia})
    return Response(status_code=HTTP_204_NO_CONTENT)
