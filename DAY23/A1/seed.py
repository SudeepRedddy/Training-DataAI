from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.students.insert_many([
    {"name": "Alice", "age": 20, "course": "Computer Science"},
    {"name": "Bob", "age": 22, "course": "Mathematics"},
    {"name": "Charlie", "age": 21, "course": "Physics"}
])

print("Sample data inserted!")
