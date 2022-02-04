from pymongo import MongoClient    # libreria para manejo de mongo mediante python

client = MongoClient('localhost:27017')    # creo la conexion
db = client.EmployeeData    # creo la base pasando  los datos  conexion.nombre de nueva base

def update():   # funcion
    # manejo de errores o excepciones
    try:    # hrealice
        criterio = input('\n Enter id to update \n')    # captura de datos
        name = input('\n Enter name to update \n')
        age = input('\n Enter age to update \n')
        country = input('\n Enter country to update \n')

        db.Employees.update_one(    # base.documento.metodo({criterio a buscar},{$set {datos nuevos}})
            {'id': criterio},
            {
                '$set': {
                    'name': name,
                    'age': age,
                    'country': country
                }
            }
        )
        print('\n Records updated successfully \n')

    except ImportError:
        platform_specific_module = None

