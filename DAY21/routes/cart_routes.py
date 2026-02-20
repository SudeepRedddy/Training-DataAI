from flask import Blueprint, jsonify

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/test', methods=['GET'])
def test_cart_route():
    return jsonify({"message": "Cart routes working!"})