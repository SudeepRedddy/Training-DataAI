from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.posts.insert_many([
    {"title": "My First Post", "content": "This is the content of my first blog post.", "comments": []},
    {"title": "Flask is Awesome", "content": "Flask makes web development simple and fun.", "comments": []}
])

print("Posts inserted!")
