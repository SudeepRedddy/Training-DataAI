from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.students.insert_many([
    {"name": "Alice", "age": 20, "course": "CS"},
    {"name": "Bob", "age": 22, "course": "Math"}
])

db.courses.insert_many([
    {"name": "Python Programming", "credits": 4, "instructor": "Dr. Sharma"},
    {"name": "Data Structures", "credits": 3, "instructor": "Prof. Kumar"}
])

print("Seed data inserted!")
