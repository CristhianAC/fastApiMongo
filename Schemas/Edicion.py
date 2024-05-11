def edicionEntity(item:dict)->dict:
    return {
        "isbn": item['isbn'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "año": item['año'],
        "idioma": item['idioma'],
        "numeroCopia": item['numeroCopia'],
        "titulo": item['titulo']
    }
def edicionesEntity(entity)->dict:
    return [edicionEntity(item) for item in entity]


    