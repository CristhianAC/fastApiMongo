


def libroEntity(item:dict)->dict:
    return {
        "id": str(item['_id']), # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "titulo": item['titulo'],
        
        
    }
def librosEntity(entity)->dict:
    return [libroEntity(item) for item in entity]