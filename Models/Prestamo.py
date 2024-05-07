from pydantic import BaseModel

class Prestamo(BaseModel):
    numeroCopia:int
    ISBN:str
    RUT:str
    fechaPrestamo:str
    fechaDevolucion:str
    