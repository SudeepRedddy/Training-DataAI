from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    products = list(db.inventory.find())
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.inventory.insert_one({
            "product_name": request.form['product_name'],
            "quantity": int(request.form['quantity']),
            "price": float(request.form['price'])
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/update_qty/<id>', methods=['POST'])
def update_qty(id):
    new_qty = int(request.form['quantity'])
    db.inventory.update_one({"_id": ObjectId(id)}, {"$set": {"quantity": new_qty}})
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    db.inventory.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
