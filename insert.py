from pymongo import mongo_client

client = mongo_client('localhost:27017')
db = client.EmployeeData

