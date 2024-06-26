from fastapi import APIRouter, Response, status
from config.db import conn

query = APIRouter()
db = conn.investigacionMongo
CONSULTA1 = [
    {
        '$lookup':{
            'from': 'autorea',
            'localField': 'titulo',
            'foreignField': 'tituloLibro',
            
            'as': 'autorea'
        }
    },
    {
        '$lookup':{
            'from': 'autor',
            'localField': 'autorea.autorNombre',
            'foreignField': 'nombre',
            'as': 'autor'
        }
    },
    {
        '$lookup': {
            'from': 'edicion',
            'localField': 'titulo',
            'foreignField': 'titulo',
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
            'localField': 'edicion.ISBN',
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
    "$lookup": {
      "from": "prestamo",
      "let": {
        "localNumero": "$copia.numero",
        "localISBN": "$copia.ISBN",
      },
      "pipeline": [
        {
          "$match": {
            "$expr": {
              "$and": [
                {
                  "$eq": [
                    "$numeroCopia",
                    "$$localNumero",
                  ],
                },
                {
                  "$eq": ["$ISBN", "$$localISBN"],
                },
              ],
            },
          },
        },
      ],
      "as": "prestamo",
    },
  },
  {
    "$match": {
      "prestamo": [],
    },
  },
  {
    "$unwind": {
      "path": "$edicion",
    },
  },
  {
    "$unwind":
      
      {
        "path": "$copia",
      },
  },
    {
        '$project':{
            '_id':0,
            'titulo': 1,
            'autor.nombre':1,
            'edicion.ISBN':1,
            'edicion.año':1,
            'edicion.idioma':1,
            'copia.numero':1
        }   
    }
]

CONSULTA2 = [
    {
        '$lookup': {
            'from': 'edicion',
            'localField': 'titulo',
            'foreignField': 'titulo',
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
            'localField': 'edicion.ISBN',
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
        '$match':{
            "usuario.RUT": ""
        }   
    },
    {
        '$project': {
            "_id": 0,
            "titulo": 1,
            
        }
    }
]
@query.get("/Query1/")
def get_copias():
    return list(db.libro.aggregate(CONSULTA1))

@query.get("/Query2/{RUT}")
def get_librosUser(RUT: str):
    CONSULTA2[8]['$match']['usuario.RUT'] = RUT
    return list(db.libro.aggregate(CONSULTA2))

