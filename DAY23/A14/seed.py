from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.inventory.insert_many([
    {"product_name": "Rice (1kg)", "quantity": 100, "price": 55.0},
    {"product_name": "Sugar (1kg)", "quantity": 80, "price": 45.0},
    {"product_name": "Oil (1L)", "quantity": 50, "price": 120.0}
])

print("Inventory inserted!")
