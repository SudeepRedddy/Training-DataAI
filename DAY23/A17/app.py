from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    category = request.args.get('category', '')
    query = {"category": category} if category else {}
    products = list(db.catalog.find(query))
    categories = db.catalog.distinct("category")
    return render_template('index.html', products=products, categories=categories, selected=category)

@app.route('/product/<id>')
def view(id):
    product = db.catalog.find_one({"_id": ObjectId(id)})
    return render_template('view.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
