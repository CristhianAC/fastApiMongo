def autoreasEntity(item:dict)->dict:
    return {
        "tituloLibro": item['tituloLibro'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "AutorNombre": item['AutorNombre'],
      
        
    }
def autoreaEntity(entity)->dict:
    return [autoreasEntity(item) for item in entity]

    