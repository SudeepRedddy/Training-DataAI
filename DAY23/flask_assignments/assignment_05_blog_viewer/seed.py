from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.blogs.insert_many([
    {"title": "First Post", "content": "Welcome to my blog! This is the first post.", "author": "Admin", "created_at": datetime.now()},
    {"title": "Flask is Awesome", "content": "Flask makes web dev simple and fun.", "author": "Dev", "created_at": datetime.now()}
])

print("Blog posts inserted!")
