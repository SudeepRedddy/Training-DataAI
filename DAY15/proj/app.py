from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from config import Config
from models import db, User, Product, Cart
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

# ---------------- FRONTEND ---------------- #

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["user_id"] = user.id
            return redirect("/products")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)

@app.route("/add-to-cart/<int:id>")
def add_to_cart(id):
    if "user_id" not in session:
        return redirect("/login")

    cart = Cart(user_id=session["user_id"], product_id=id)
    db.session.add(cart)
    db.session.commit()
    return redirect("/products")

@app.route("/cart")
def view_cart():
    if "user_id" not in session:
        return redirect("/login")

    carts = Cart.query.filter_by(user_id=session["user_id"]).all()
    products = []
    total = 0

    for c in carts:
        product = Product.query.get(c.product_id)
        products.append(product)
        total += product.price

    return render_template("cart.html", products=products, total=total)

@app.route("/checkout")
def checkout():
    return "<h2>Checkout Successful!</h2><a href='/products'>Continue Shopping</a>"

# ---------------- REST API ---------------- #

@app.route("/api/register", methods=["POST"])
def api_register():
    data = request.json
    password = generate_password_hash(data["password"])
    user = User(username=data["username"], password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User Created"), 201

@app.route("/api/login", methods=["POST"])
def api_login():
    user = User.query.filter_by(username=request.json["username"]).first()

    if user and check_password_hash(user.password, request.json["password"]):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)

    return jsonify(message="Invalid Credentials"), 401

@app.route("/api/products", methods=["GET"])
def get_products():
    min_price = request.args.get("min_price")
    query = Product.query

    if min_price:
        query = query.filter(Product.price >= float(min_price))

    products = query.all()
    return jsonify([{"id":p.id,"name":p.name,"price":p.price} for p in products])

@app.route("/api/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.json
    product = Product(name=data["name"], price=data["price"])
    db.session.add(product)
    db.session.commit()
    return jsonify(message="Product Created"), 201

@app.route("/api/products/<int:id>", methods=["PUT"])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    product.name = request.json.get("name", product.name)
    product.price = request.json.get("price", product.price)
    db.session.commit()
    return jsonify(message="Updated")

@app.route("/api/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify(message="Deleted")

if __name__ == "__main__":
    app.run(debug=True)
