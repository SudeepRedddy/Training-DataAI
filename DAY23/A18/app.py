from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    enrollments = list(db.enrollments.find())
    for e in enrollments:
        s = db.students.find_one({"_id": ObjectId(e['student_id'])})
        c = db.courses.find_one({"_id": ObjectId(e['course_id'])})
        e['student_name'] = s['name'] if s else 'Unknown'
        e['course_name'] = c['name'] if c else 'Unknown'
    return render_template('index.html', enrollments=enrollments)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        db.enrollments.insert_one({
            "student_id": request.form['student_id'],
            "course_id": request.form['course_id'],
            "enrolled_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return redirect('/')
    students = list(db.students.find())
    courses = list(db.courses.find())
    return render_template('enroll.html', students=students, courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
