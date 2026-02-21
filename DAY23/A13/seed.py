from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.movies.insert_many([
    {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action", "rating": 9.0},
    {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "genre": "Sci-Fi", "rating": 8.6}
])

print("Movies inserted!")
