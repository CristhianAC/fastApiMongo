from pydantic import BaseModel

class Prestamo(BaseModel):
    numeroCopia:int
    RUT:str
    fechaPrestamo:str
    fechaDevolucion:str
    