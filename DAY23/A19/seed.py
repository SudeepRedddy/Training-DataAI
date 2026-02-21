from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

db.events.insert_many([
    {"title": "Tech Fest 2025", "description": "Annual tech festival", "event_date": "2025-08-15", "location": "Hyderabad", "organizer": "IIIT"},
    {"title": "Python Workshop", "description": "Python for beginners", "event_date": "2025-09-01", "location": "Online", "organizer": "CodeClub"}
])

print("Events inserted!")
