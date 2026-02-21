from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.quotes.insert_many([
    {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"}
])

print("Quotes inserted!")
