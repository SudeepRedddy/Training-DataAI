from flask import Blueprint, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/test', methods=['GET'])
def test_user_route():
    return jsonify({"message": "User routes working!"})