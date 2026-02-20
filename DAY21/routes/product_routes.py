from flask import Blueprint, jsonify

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/test', methods=['GET'])
def test_product_route():
    return jsonify({"message": "Product routes working!"})