from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.catalog.insert_many([
    {"name": 'Samsung TV 43"', "price": 35000, "category": "Electronics", "description": "4K Smart TV", "stock": 10},
    {"name": "Nike Running Shoes", "price": 4500, "category": "Footwear", "description": "Lightweight running shoes", "stock": 25},
    {"name": "Python Book", "price": 800, "category": "Books", "description": "Learn Python in 30 days", "stock": 50},
    {"name": "Sony Headphones", "price": 8000, "category": "Electronics", "description": "Noise cancelling headphones", "stock": 15}
])

print("Catalog inserted!")
