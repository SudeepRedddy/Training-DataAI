from flask import Flask, jsonify
from config import Config
from utils.db import get_db, close_db


from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.cart_routes import cart_bp
from routes.order_routes import order_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        try:
            db = get_db()
            # The 'ping' command is a lightweight way to check if the server is alive
            db.command('ping')
            print("MongoDB connected successfully!")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            # In a real application, you might want to log this error and potentially
            # prevent the app from starting if the database is critical.

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(cart_bp, url_prefix='/api/cart')
    app.register_blueprint(order_bp, url_prefix='/api/orders')

    # Teardown database connection
    app.teardown_appcontext(close_db)

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to FlaskCart API!"})

    @app.route('/health')
    def health_check():
        try:
            db = get_db()
            db.command('ping')
            return jsonify({"status": "ok", "database": "connected"}), 200
        except Exception as e:
            return jsonify({"status": "error", "database": "disconnected", "details": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])