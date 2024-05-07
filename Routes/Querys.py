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
            'from': 'prestamo',
            'localField': 'RUT',
            'foreignField': 'RUT',
            'as': 'prestamo'
        }
    },
    {
        '$unwind': '$prestamo'  # Desenrollar el array 'prestamo'
    },
    {
        '$lookup': {
            'from': 'copia',
            'localField': 'prestamo.numeroCopia',
            'foreignField': 'numero',
            'as': 'copia'
        }
    },
    {
        '$unwind': '$copia'  # Desenrollar el array 'copia'
    },
    {
        '$match': {
            'copia.ISBN': '$prestamo.ISBN'
        }
    },
    {
        '$lookup': {
            'from': 'edicion',
            'localField': 'copia.ISBN',
            'foreignField': 'ISBN',
            'as': 'edicion'
        }
    },
    {
        '$unwind': '$edicion'  # Desenrollar el array 'edicion'
    },
    {
        '$lookup': {
            'from': 'libro',
            'localField': 'edicion.ISBN',
            'foreignField': 'editorial',
            'as': 'libro'
        }
    },
    {
        '$unwind': '$libro'  # Desenrollar el array 'libro'
    },
    {
        '$project': {
            '_id': 0,
            'libro.titulo': 1
        }
    }
]

@query.get("/prestamos/{RUT}")
def get_librosUser():
    return db.usuario.aggregate(CONSULTA2)