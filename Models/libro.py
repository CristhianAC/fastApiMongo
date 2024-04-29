from pydantic import BaseModel

class libro(BaseModel):
    titulo: str
    autor: str
    editorial: str
    