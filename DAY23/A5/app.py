from flask import Flask, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    blogs = list(db.blogs.find().sort("created_at", -1))
    return render_template('index.html', blogs=blogs)

@app.route('/blog/<id>')
def view(id):
    blog = db.blogs.find_one({"_id": ObjectId(id)})
    return render_template('view.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)
