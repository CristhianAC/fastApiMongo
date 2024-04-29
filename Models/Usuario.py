from pydantic import BaseModel

class Usuario(BaseModel):
    RUT:str
    nombre:str
    