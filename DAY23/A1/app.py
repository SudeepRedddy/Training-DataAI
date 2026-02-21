from flask import Flask, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    students = list(db.students.find())
    return render_template('index.html', students=students)

@app.route('/student/<id>')
def view_student(id):
    student = db.students.find_one({"_id": ObjectId(id)})
    return render_template('view.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
