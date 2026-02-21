from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    students = list(db.students.find())
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.students.insert_one({
            "name": request.form['name'],
            "age": int(request.form['age']),
            "course": request.form['course']
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        db.students.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": request.form['name'], "age": int(request.form['age']), "course": request.form['course']}}
        )
        return redirect('/')
    student = db.students.find_one({"_id": ObjectId(id)})
    return render_template('edit.html', student=student)

@app.route('/delete/<id>')
def delete(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
