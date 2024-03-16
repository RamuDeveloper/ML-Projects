
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["Employees"]
collection=db["data"]

Employee_Data=[
    {"Name":"Venugopal","age":25,"Salary":50000},
    {"Name":"Ramu","age":23,"Salary":15000},
    {"Name":"Shyamu","age":22,"Salary":150000}
]

collection.insert_many(Employee_Data)


