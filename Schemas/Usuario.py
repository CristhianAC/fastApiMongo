def usuarioEntity(item:dict)->dict:
    return {
        "RUT": item['RUT'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "nombre": item['nombre'],
        
    }
def usuariosEntity(entity)->dict:
    return [usuarioEntity(item) for item in entity]

