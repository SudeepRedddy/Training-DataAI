from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    books = list(db.books.find())
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.books.insert_one({
            "title": request.form['title'],
            "author": request.form['author'],
            "genre": request.form['genre'],
            "year": int(request.form['year'])
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<id>')
def delete(id):
    db.books.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
