from flask import Blueprint, jsonify

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/test', methods=['GET'])
def test_order_route():
    return jsonify({"message": "Order routes working!"})