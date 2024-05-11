from fastapi import APIRouter, Response, status
from config.db import conn
from Schemas.Usuario import usuarioEntity, usuariosEntity
from Models.Usuario import Usuario
user = APIRouter()
db = conn.investigacionMongo.usuario
dbP = conn.investigacionMongo.prestamo
@user.get("/usuarios")
def get_users():
    return usuariosEntity(db.find({},{}))
@user.post("/usuarios")
def post_users(usuario: Usuario):
    new_usuario = dict(usuario)
    id = db.insert_one(new_usuario).inserted_id
    return str(id)
@user.get("/usuarios/{RUT}")
def get_user(RUT:str):
    return usuarioEntity(db.find_one({"RUT":RUT},{}))
@user.put("/usuarios/{RUT}")
def update_user(RUT:str, usuario:Usuario):
    db.find_one_and_update({"RUT":RUT},{"$set": dict(usuario)})
    dbP.update_many({"RUT":RUT},{"$set": {'RUT':usuario.RUT}})
@user.delete("/usuarios/{RUT}")
def delete_user(RUT:str):
    dbP.delete_many({"RUT":RUT})
    db.find_one_and_delete({"RUT":RUT})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
