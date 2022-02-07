from pymongo import MongoClient    # libreria para manejo de mongo mediante python

client = MongoClient('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def delete():   # funcion
    # manejo de errores o excepciones
    try:    # realice
        criterio = input('\n Enter employed id to delete \n')   # captura de dato para borrar
        db.Employees.delete_many({'id': criterio})  # eliminar registro  base.documento.modulo(registro seleccionado)
        print('\n Deletion Successful \n')
    except ImportError: # manejo de errores por codigo
        platform_specific_module = None