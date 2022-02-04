from platform import platform
from pymongo import mongo_client    # libreria para manejo de mongo mediante python

client = mongo_client('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def read():
    try:
        emp_lista = db.Employees.find()
        print('\n All data from EmployeeData DataBase \n')
        for emp in emp_lista:
            print(emp)

    except ImportError:
        platform_specific_module = None