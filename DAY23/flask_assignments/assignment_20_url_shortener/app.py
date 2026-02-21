from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from datetime import datetime
import random, string

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskdb"]

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['url']
        code = generate_code()
        db.urls.insert_one({
            "original_url": original_url,
            "short_code": code,
            "created_at": datetime.now(),
            "click_count": 0
        })
        short_url = f"http://localhost:5000/{code}"
    urls = list(db.urls.find().sort("created_at", -1).limit(10))
    return render_template('index.html', urls=urls, short_url=short_url)

@app.route('/<code>')
def redirect_url(code):
    url = db.urls.find_one({"short_code": code})
    if url:
        db.urls.update_one({"short_code": code}, {"$inc": {"click_count": 1}})
        return redirect(url['original_url'])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
