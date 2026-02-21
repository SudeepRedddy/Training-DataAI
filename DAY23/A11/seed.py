from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.books.insert_many([
    {"title": "Python Crash Course", "author": "Eric Matthes", "genre": "Programming", "year": 2019},
    {"title": "Clean Code", "author": "Robert Martin", "genre": "Programming", "year": 2008},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help", "year": 2018}
])

print("Books inserted!")
