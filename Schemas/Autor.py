def autorEntity(item:dict)->dict:
    return {
        'nombre': item['nombre'],
        
    }
def autoresEntity(entity)->dict:
    return [autorEntity(item) for item in entity]