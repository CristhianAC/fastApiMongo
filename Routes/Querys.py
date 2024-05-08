from fastapi import APIRouter, Response, status
from config.db import conn

query = APIRouter()
db = conn.investigacionMongo
CONSULTA1 = [
    {
    
    }
]

CONSULTA2 = [
    {
        '$lookup': {
            'from': 'edicion',
            'localField': 'editorial',
            'foreignField': 'isbn',
            'as': 'edicion'
        }
    },
    {
        '$match': {
            'edicion': {'$ne': []}
        }
    },
    {
        '$lookup': {
            'from': 'copia',
            'localField': 'edicion.isbn',
            'foreignField': 'ISBN',
            'as': 'copia'
        }
    },
    {
        '$match': {
            'copia': {'$ne': []}
        }
    },
    {
        '$lookup': {
            'from': 'prestamo',
            'localField': 'copia.ISBN',
            'foreignField': 'ISBN',
            'as': 'prestamo'
        }
    },
    {
        '$match': {
            '$expr': {
                '$eq': ['$copia.numero', '$prestamo.numeroCopia']
            }
        }
    },
    {
        '$lookup':{
            'from': 'usuario',
            'localField': 'prestamo.RUT',
            'foreignField':'RUT',
            'as':'usuario'
        }
    },
    {
        '$match':{
            'usuario':{
                '$ne':[]
            }
        }

    },
    {
        '$project': {
            "_id": 0,
            "titulo": 1,
            
        }
    }
]

@query.get("/Query2/{RUT}")
def get_librosUser(RUT: str):
    return list(db.prestamo.autor.aggregate([
        {'$match': {'RUT': RUT}},
    ] + CONSULTA2))
