from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Edicion import edicionEntity, edicionesEntity
from Models.Edicion import Edicion
from starlette.status import HTTP_204_NO_CONTENT
edicion = APIRouter()
db = conn.investigacionMongo.edicion
dbL = conn.investigacionMongo.libro
dbC = conn.investigacionMongo.copia
dbP = conn.investigacionMongo.prestamo
@edicion.get("/ediciones")
def get_ediciones():
    return edicionesEntity(db.find({},{}))


@edicion.post("/ediciones")
def post_ediciones(edicion: Edicion):
    new_edicion = dict(edicion)
    id = db.insert_one(new_edicion).inserted_id
    return str(id)
@edicion.get("/ediciones/{ISBN}")
def get_edicion(ISBN:str):
    return edicionEntity(db.find_one({"ISBN":ISBN},{}))
@edicion.put("/ediciones/{ISBN}")
def update_edicion(ISBN:str, edicion:Edicion):
    db.find_one_and_update({"ISBN":ISBN},{"$set": dict(edicion)})
    dbC.update_many({"ISBN":ISBN},{"$set": {'ISBN':edicion.ISBN}})
@edicion.delete("/ediciones/{ISBN}")
def delete_edicion(ISBN:str):
    dbP.delete_many({"ISBN":ISBN})
    dbC.delete_many({"ISBN":ISBN})
    db.find_one_and_delete({"ISBN":ISBN})
    return Response(status_code=HTTP_204_NO_CONTENT)
