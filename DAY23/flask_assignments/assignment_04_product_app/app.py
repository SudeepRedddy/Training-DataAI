from flask import Flask, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    products = list(db.products.find())
    return render_template('index.html', products=products)

@app.route('/product/<id>')
def view(id):
    product = db.products.find_one({"_id": ObjectId(id)})
    return render_template('view.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
