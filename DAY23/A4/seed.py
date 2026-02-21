from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.products.insert_many([
    {"name": "Laptop", "price": 55000, "description": "High-performance laptop"},
    {"name": "Phone", "price": 15000, "description": "Smartphone with AMOLED"},
    {"name": "Tablet", "price": 25000, "description": "10-inch display tablet"}
])

print("Products inserted!")
