def prestamoEntity(item:dict)->dict:
    return {
        "RUT": item['RUT'], # Convertir el ObjectId de mongo en un string para que pueda ser serializado a JSON
        "numeroCopia": item['numeroCopia'],
        "fechaPrestamo": item['fechaPrestamo'],
        "fechaDevolucion": item['fechaDevolucion'],
        
        
    }
def prestamosEntity(entity)->dict:
    return [prestamoEntity(item) for item in entity]


