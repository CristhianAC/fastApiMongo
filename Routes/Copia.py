from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Copia import copiaEntity, copiasEntity
from Models.Copia import Copia
from starlette.status import HTTP_204_NO_CONTENT
copia = APIRouter()
db = conn.investigacionMongo.copia

@copia.get("/copias")
def get_copias():
    return copiasEntity(db.find({},{}))
@copia.post("/copias")
def post_copias(copia: Copia):
    new_copia = dict(copia)
    id = db.insert_one(new_copia).inserted_id
    return str(id)
@copia.get("/copias/{titulo}")
def get_copia(titulo:str):
    return copiaEntity(db.find_one({"titulo":titulo},{}))

@copia.put("/copias/{titulo}")
def update_copia(titulo:str, copia:Copia):
    db.find_one_and_update({"titulo":titulo},{"$set": dict(copia)})

@copia.delete("/copias/{titulo}")
def delete_copia(titulo:str):
    db.find_one_and_delete({"titulo":titulo})
    return Response(status_code=HTTP_204_NO_CONTENT)