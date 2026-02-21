from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.tasks.insert_one({"title": request.form['title'], "status": "pending"})
        return redirect('/')
    tasks = list(db.tasks.find())
    return render_template('index.html', tasks=tasks)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        db.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"title": request.form['title']}})
        return redirect('/')
    task = db.tasks.find_one({"_id": ObjectId(id)})
    return render_template('edit.html', task=task)

@app.route('/delete/<id>')
def delete(id):
    db.tasks.delete_one({"_id": ObjectId(id)})
    return redirect('/')

@app.route('/complete/<id>')
def complete(id):
    db.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"status": "completed"}})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
