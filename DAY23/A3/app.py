from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    contacts = list(db.contacts.find())
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.contacts.insert_one({
            "name": request.form['name'],
            "phone": request.form['phone'],
            "email": request.form['email']
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/contact/<id>')
def view(id):
    contact = db.contacts.find_one({"_id": ObjectId(id)})
    return render_template('view.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True)
