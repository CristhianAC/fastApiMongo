from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Autor import autorEntity, autoresEntity
from Models.Autor import Autor
author = APIRouter()
db = conn.investigacionMongo.autor

@author.get("/autores")
def get_authors():
    return autoresEntity(db.find({},{}))
@author.post("/autores")
def post_authors(autor: Autor):
    new_autor = dict(autor)
    id = db.insert_one(new_autor).inserted_id
    return str(id)
@author.get("/autores/{nombre}")
def get_author(nombre:str):
    return autorEntity(db.find_one({"nombre":nombre},{}))
@author.put("/autores/{nombre}")
def update_author(nombre:str, autor:Autor):
    db.find_one_and_update({"nombre":nombre},{"$set": dict(autor)})

@author.delete("/autores/{nombre}")
def delete_author(nombre:str):
    db.find_one_and_delete({"nombre":nombre})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

