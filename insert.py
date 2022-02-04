from pymongo import MongoClient    # libreria para manejo de mongo mediante python

client = MongoClient('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def insert():   # funcion
    try:    # manejo de errores
        # captura de datos
        employee_id = input('Enter employed id: ')
        employee_name = input('Enter name: ')
        employee_country = input('Enter country: ')
        employee_age = input('Enter age: ')

        db.Employees.insert_one(    # pasar mediante json los datos a la base  base.documento.metoodo({})
        {
            'id': employee_id,
            'name': employee_name,
            'country': employee_country,
            'age': employee_age

        })
        print('Inserted data successfully') # mensaje al completar la inserccion

    except ImportError: # control de errores
        platform_specific_module = None