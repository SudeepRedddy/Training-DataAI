from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        db.todos.insert_one({"title": title, "status": "pending"})
        return redirect('/')
    todos = list(db.todos.find())
    return render_template('index.html', todos=todos)

@app.route('/delete/<id>')
def delete(id):
    db.todos.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
