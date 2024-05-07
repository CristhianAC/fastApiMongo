def copiaEntity(item:dict)->dict:
    return {
        "numero": item['numero'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "ISBN": item['ISBN'] 
       
    }
def copiasEntity(entity)->dict:
    return [copiaEntity(item) for item in entity]