from flask import jsonify, request
from . import users_bp
from .services import create_user_service, get_user_service, delete_user_service

@users_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    email    = data.get('email')
    password = data.get('password')

    if not data:
        return jsonify({'message': 'Data is required'}), 400

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = create_user_service(email, password)

    return jsonify(user.to_dict()), 201

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