from flask import jsonify, request
from . import users_bp
from .services import create_user_service, get_user_service, delete_user_service, register_paypay_url_service
from app.util import add_success, return_failure

@users_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    line_token = data.get('line_token')

    if not data:
        return return_failure(), 400

    if not line_token:
        return return_failure(), 400

    user = create_user_service(line_token)
    
    return add_success(user.to_dict()), 201

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_service(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    Is_deleted = delete_user_service(user_id)
    if Is_deleted:
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    
@users_bp.route('/users/<int:user_id>/paypay-link', methods=['POST'])
def register_paypay_url(user_id):
    data = request.json
    paypay_url = data.get('paypayLink')

    if not data:
        return jsonify({'isSuccessful': False}), 400

    if not paypay_url:
        return jsonify({'isSuccessful': False}), 400

    user = register_paypay_url_service(user_id, paypay_url)

    if user:
        return jsonify(dict(**{'isSuccessful':True},**user.to_dict())), 200
    else:
        return jsonify({'isSuccessful': False}), 404