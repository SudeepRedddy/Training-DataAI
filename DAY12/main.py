from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/about")
def about():
    return "About Page!"

@app.route("/about/<name>")
def user(name):
    return f"Hello,{name}"

@app.route("/hello")
def check():
    return render_template("index.html",name = "Sudeep")


@app.route("/for")
def fors():
    return render_template("form.html")

@app.route("/submit",methods = ["POST"])
def submit():
    username =request.form["username"]
    return f"Hello,{username}"

@app.route("/uploa")
def upload():
    return render_template("upload.html")

@app.route("/uploaded",methods = ["POST"])
def uploaded():
    file = request.files["file"]
    return file.filename


if __name__ == "__main__":
    app.run(debug=True)