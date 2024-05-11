from pydantic import BaseModel

class Edicion(BaseModel):
    ISBN: str
    año: str
    idioma: str
    numeroCopia:int
    titulo: str
    