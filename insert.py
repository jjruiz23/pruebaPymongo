from pymongo import mongo_client

client = mongo_client('localhost:27017')
db = client.EmployeeData

def insert():
    try:
        employee_id = input('Enter employed id: ')
        employee_name = input('Enter name: ')
        employee_country = input('Enter country: ')
        employee_age = input('Enter age: ')

        db.Employees.insert_one(
        {
            'id': employee_id,
            'name': employee_name,
            'couentry': employee_country,
            'age': employee_age

        })
        print('Inserted data successfully')

    except ImportError:
        platform_specific_module = None