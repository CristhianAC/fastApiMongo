from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Usuario import usuarioEntity, usuariosEntity
from Models.Usuario import Usuario
user = APIRouter()
db = conn.investigacionMongo.usuario

@user.get("/usuarios")
def get_users():
    return usuariosEntity(db.find({},{}))
@user.post("/usuarios")
def post_users(usuario: Usuario):
    new_usuario = dict(usuario)
    id = db.insert_one(new_usuario).inserted_id
    return str(id)
@user.get("/usuarios/{nombre}")
def get_user(nombre:str):
    return usuarioEntity(db.find_one({"nombre":nombre},{}))
@user.put("/usuarios/{nombre}")
def update_user(nombre:str, usuario:Usuario):
    db.find_one_and_update({"nombre":nombre},{"$set": dict(usuario)})
@user.delete("/usuarios/{nombre}")
def delete_user(nombre:str):
    db.find_one_and_delete({"nombre":nombre})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
