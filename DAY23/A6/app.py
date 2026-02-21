from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    dept = request.args.get('dept', '')
    query = {"department": dept} if dept else {}
    employees = list(db.employees.find(query))
    departments = db.employees.distinct("department")
    return render_template('index.html', employees=employees, departments=departments, selected=dept)

if __name__ == '__main__':
    app.run(debug=True)
