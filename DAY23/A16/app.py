from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    posts = list(db.posts.find())
    return render_template('index.html', posts=posts)

@app.route('/post/<id>', methods=['GET', 'POST'])
def view(id):
    if request.method == 'POST':
        comment = {
            "author": request.form['author'],
            "body": request.form['body'],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        db.posts.update_one({"_id": ObjectId(id)}, {"$push": {"comments": comment}})
        return redirect(f'/post/{id}')
    post = db.posts.find_one({"_id": ObjectId(id)})
    return render_template('view.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
