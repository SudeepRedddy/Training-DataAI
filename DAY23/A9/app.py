from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

@app.route('/')
def index():
    posts = list(db.blog_posts.find().sort("created_at", -1))
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.blog_posts.insert_one({
            "title": request.form['title'],
            "content": request.form['content'],
            "author": request.form['author'],
            "created_at": datetime.now()
        })
        return redirect('/')
    return render_template('add.html')

@app.route('/view/<id>')
def view(id):
    post = db.blog_posts.find_one({"_id": ObjectId(id)})
    return render_template('view.html', post=post)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        db.blog_posts.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"title": request.form['title'], "content": request.form['content']}}
        )
        return redirect('/')
    post = db.blog_posts.find_one({"_id": ObjectId(id)})
    return render_template('edit.html', post=post)

@app.route('/delete/<id>')
def delete(id):
    db.blog_posts.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
