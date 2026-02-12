from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pydantic import BaseModel, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# =======================
# DATABASE MODELS
# =======================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20), default="user")

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =======================
# PYDANTIC MODEL
# =======================

class ItemSchema(BaseModel):
    name: str
    price: float
    description: str

# =======================
# FRONTEND ROUTES
# =======================

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for('register'))

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully")
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('products'))
        flash("Invalid credentials")

    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/products')
@login_required
def products():
    items = Item.query.all()
    return render_template("products.html", items=items)

@app.route('/add_to_cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    cart_item = Cart(user_id=current_user.id, item_id=item_id, quantity=1)
    db.session.add(cart_item)
    db.session.commit()
    flash("Item added to cart")
    return redirect(url_for('products'))

@app.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    items = []
    total = 0
    for c in cart_items:
        item = Item.query.get(c.item_id)
        total += item.price * c.quantity
        items.append((item, c.quantity))
    return render_template("cart.html", items=items, total=total)

@app.route('/remove_from_cart/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    Cart.query.filter_by(user_id=current_user.id, item_id=item_id).delete()
    db.session.commit()
    flash("Removed from cart")
    return redirect(url_for('cart'))

@app.route('/checkout')
@login_required
def checkout():
    return render_template("checkout.html")

@app.route('/payment', methods=['POST'])
@login_required
def payment():
    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash("Payment Successful!")
    return redirect(url_for('products'))

# =======================
# UPLOAD FORM
# =======================

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file.filename == "":
            flash("No file selected")
            return redirect(url_for('upload'))
        return render_template("results.html", filename=file.filename)
    return render_template("upload.html")

# =======================
# REST API
# =======================

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{
        "id": i.id,
        "name": i.name,
        "price": i.price,
        "description": i.description
    } for i in items])

@app.route('/api/items', methods=['POST'])
def create_item():
    try:
        data = ItemSchema(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    item = Item(name=data.name, price=data.price, description=data.description)
    db.session.add(item)
    db.session.commit()
    return jsonify({"message":"Item created"}), 201

@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    try:
        data = ItemSchema(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    item.name = data.name
    item.price = data.price
    item.description = data.description
    db.session.commit()
    return jsonify({"message":"Updated"})

@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message":"Deleted"})

# =======================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
