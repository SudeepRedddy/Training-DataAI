from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    result = list(db.quotes.aggregate([{"$sample": {"size": 1}}]))
    quote = result[0] if result else None
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
