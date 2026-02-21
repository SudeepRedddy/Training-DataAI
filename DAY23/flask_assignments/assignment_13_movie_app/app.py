from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    movies = list(db.movies.find())
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.movies.insert_one({
            "title": request.form['title'],
            "director": request.form['director'],
            "year": int(request.form['year']),
            "genre": request.form['genre'],
            "rating": float(request.form['rating'])
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/movie/<id>')
def view(id):
    movie = db.movies.find_one({"_id": ObjectId(id)})
    return render_template('view.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
