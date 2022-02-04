from platform import platform
from pymongo import mongo_client    # libreria para manejo de mongo mediante python

client = mongo_client('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def delete():

    try:
        criterio = input('\N Enter employed id to delete \n')
        db.Employees.delete_many({'id': criterio})
        print('\n Deletion Successful \n')
    except ImportError:
        platform_specific_module = None