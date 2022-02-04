from pymongo import MongoClient    # libreria para manejo de mongo mediante python

client = MongoClient('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def read(): # funcion
    #menejo de exceciones error
    try:    # realice
        emp_lista = db.Employees.find() # buscar datos de documento   base.documento.buscar()
        print('\n All data from EmployeeData DataBase \n')  # mensaje
        for emp in emp_lista:   # recorrer los datos almacenados en la busqueda
            print(emp)  # impimir dato en cada paso del recorrido

    except ImportError: # manejo de errores
        platform_specific_module = None