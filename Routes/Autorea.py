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

@autorea.get("/autoreas/{tituloLibro}")
def get_autorea(tituloLibro:str):
    return autoreaEntity(db.find_one({"tituloLibro":tituloLibro},{}))

@autorea.put("/autoreas/{tituloLibro}/{nombreAutor}")
def update_autorea(tituloLibro:str,nombreAutor:str, autorea:Autorea):
    db.find_one_and_update({"tituloLibro":tituloLibro,"nombreAutor":nombreAutor},{"$set": dict(autorea)})
    
@autorea.delete("/autoreas/{tituloLibro}/{nombreAutor}")
def delete_autorea(tituloLibro:str, nombreAutor:str):
    db.delete_many({"tituloLibro":tituloLibro,"autorNombre":nombreAutor})
    return Response(status_code=HTTP_204_NO_CONTENT)
