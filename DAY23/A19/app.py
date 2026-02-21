from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    events = list(db.events.find().sort("event_date", 1))
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.events.insert_one({
            "title": request.form['title'],
            "description": request.form['description'],
            "event_date": request.form['event_date'],
            "location": request.form['location'],
            "organizer": request.form['organizer']
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<id>')
def delete(id):
    db.events.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
