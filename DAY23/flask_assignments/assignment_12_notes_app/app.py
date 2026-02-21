from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.notes.insert_one({
            "title": request.form['title'],
            "content": request.form['content'],
            "created_at": datetime.now()
        })
        return redirect('/')
    notes = list(db.notes.find().sort("created_at", -1))
    return render_template('index.html', notes=notes)

@app.route('/delete/<id>')
def delete(id):
    db.notes.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
