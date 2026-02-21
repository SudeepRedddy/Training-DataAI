from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.employees.insert_many([
    {"name": "Ravi", "department": "IT", "position": "Developer", "salary": 45000},
    {"name": "Priya", "department": "HR", "position": "Manager", "salary": 55000},
    {"name": "Sami", "department": "IT", "position": "Analyst", "salary": 40000},
    {"name": "Anita", "department": "Finance", "position": "Accountant", "salary": 50000}
])

print("Employees inserted!")
