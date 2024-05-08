from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Copia import copiaEntity, copiasEntity
from Models.Copia import Copia
from starlette.status import HTTP_204_NO_CONTENT
copia = APIRouter()
db = conn.investigacionMongo.copia
dbc = conn.investigacionMongo.prestamo
@copia.get("/copias")
def get_copias():
    return copiasEntity(db.find({},{}))
@copia.post("/copias")
def post_copias(copia: Copia):
    new_copia = dict(copia)
    id = db.insert_one(new_copia).inserted_id
    return str(id)
@copia.get("/copias/{numero}")
def get_copia(numero:int):
    return copiaEntity(db.find_one({"numero":numero},{}))

@copia.put("/copias/{numero}")
def update_copia(numero:int, copia:Copia):
    db.find_one_and_update({"numero":numero},{"$set": dict(copia)})

@copia.delete("/copias/{numero}/{ISBN}")
def delete_copia(numero:int, ISBN:str):
    db.find_one_and_delete({"numero":numero, "ISBN":ISBN})
    dbc.find_one_and_delete({"numeroCopia":numero, "ISBN":ISBN})
    return Response(status_code=HTTP_204_NO_CONTENT)