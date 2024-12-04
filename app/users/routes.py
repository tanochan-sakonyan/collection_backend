from asyncio import Event
from flask import jsonify, request
from . import users_bp
from .services import create_user_service, get_user_service, delete_user_service, register_paypay_url_service
from app.util import add_success, return_failure
from app import db

@users_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json

    if not data:
        return return_failure(), 400

    line_token = data.get('line_token')
    if not line_token:
        return return_failure(), 400

    try:
        user = create_user_service(line_token)
        if not user.events or len(user.events) == 0:
            default_event = Event(
                event_name="一次会",
                members=[]
            )
            user.events.append(default_event)
            db.session.commit()

        return add_success(user.to_dict()), 201
    except Exception as e:
        # ログに詳細を記録
        users_bp.logger.error(f"Error in create_user: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = get_user_service(user_id)
        if user:
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        users_bp.logger.error(f"Error in get_user: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        is_deleted = delete_user_service(user_id)
        if is_deleted:
            return jsonify({'message': 'User deleted'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        users_bp.logger.error(f"Error in delete_user: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@users_bp.route('/users/<int:user_id>/paypay-link', methods=['POST'])
def register_paypay_url(user_id):
    data = request.json

    if not data:
        return jsonify({'isSuccessful': False}), 400

    paypay_url = data.get('paypayLink')
    if not paypay_url:
        return jsonify({'isSuccessful': False}), 400

    try:
        user = register_paypay_url_service(user_id, paypay_url)
        if user:
            return jsonify(dict(**{'isSuccessful':True},**user.to_dict())), 200
        else:
            return jsonify({'isSuccessful': False}), 404
    except Exception as e:
        users_bp.logger.error(f"Error in register_paypay_url: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
