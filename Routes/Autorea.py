from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Autorea import autoreaEntity, autoreasEntity
from Models.Autorea import Autorea
from starlette.status import HTTP_204_NO_CONTENT
autorea = APIRouter()
db = conn.investigacionMongo.autorea

@autorea.get("/autoreas")
def get_autoreas():
    return autoreasEntity(db.find({},{}))

@autorea.post("/autoreas")
def post_autoreas(autorea: Autorea):
    new_autorea = dict(autorea)
    id = db.insert_one(new_autorea).inserted_id
    return str(id)

@autorea.get("/autoreas/{nombre}")
def get_autorea(nombre:str):
    return autoreaEntity(db.find_one({"nombre":nombre},{}))

@autorea.put("/autoreas/{nombre}")
def update_autorea(nombre:str, autorea:Autorea):
    db.find_one_and_update({"nombre":nombre},{"$set": dict(autorea)})
    
@autorea.delete("/autoreas/{nombre}")
def delete_autorea(nombre:str):
    db.find_one_and_delete({"nombre":nombre})
    return Response(status_code=HTTP_204_NO_CONTENT)
