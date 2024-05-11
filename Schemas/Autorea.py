def autoreaEntity(item:dict)->dict:
    return {
        "tituloLibro": item['tituloLibro'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "autorNombre": item['autorNombre'],
      
        
    }
def autoreasEntity(entity)->dict:
    return [autoreaEntity(item) for item in entity]

    