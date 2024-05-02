from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Edicion import edicionEntity, edicionesEntity
from Models.Edicion import Edicion
from starlette.status import HTTP_204_NO_CONTENT
edicion = APIRouter()
db = conn.investigacionMongo.edicion

@edicion.get("/ediciones")
def get_ediciones():
    return edicionesEntity(db.find({},{}))
@edicion.post("/ediciones")
def post_ediciones(edicion: Edicion):
    new_edicion = dict(edicion)
    id = db.insert_one(new_edicion).inserted_id
    return str(id)
@edicion.get("/ediciones/{titulo}")
def get_edicion(titulo:str):
    return edicionEntity(db.find_one({"titulo":titulo},{}))
@edicion.put("/ediciones/{titulo}")
def update_edicion(titulo:str, edicion:Edicion):
    db.find_one_and_update({"titulo":titulo},{"$set": dict(edicion)})
@edicion.delete("/ediciones/{titulo}")
def delete_edicion(titulo:str):
    db.find_one_and_delete({"titulo":titulo})
    return Response(status_code=HTTP_204_NO_CONTENT)
