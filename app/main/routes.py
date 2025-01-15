from flask import jsonify, request
from . import main
from .service import register_paypay_url_service, create_event_service, delete_event_service, \
    create_member_service, get_member_service, delete_member_service, update_member_service, change_member_status_service
from collections import defaultdict

@main.route('/users/<string:user_id>/paypay-link', methods=['POST'])
def register_paypay_url(user_id):
    data = request.json

    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    paypay_url = data.get('paypayLink')

    if not paypay_url:
        return jsonify({'isSuccessful': False}), 400
    
    try:
        all_user_info = register_paypay_url_service(user_id, paypay_url)
        if all_user_info:
            return jsonify(dict(**{'isSuccessful': True}, **all_user_info)), 200
        else:
            return jsonify({'isSuccessful': False}), 404
        
    except Exception as e:
        main.logger.error(f"Error in register_paypay_url: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    

@main.route('/users/<string:user_id>/events', methods=['POST'])
def create_event(user_id):
    data = request.json

    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    event_name = data.get('eventName')

    if not event_name or not user_id:
        return jsonify({'isSuccessful': False}), 400
    
    try:
        event_info = create_event_service(event_name, user_id)
        return jsonify(dict(**{'isSuccessful': True}, **event_info)), 201
    
    except Exception as e:
        main.logger.error(f"Error in create_event: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    
@main.route('/users/<string:user_id>/events', methods=['DELETE'])
def delete_event(user_id):
    data = request.json

    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    event_id_list = data.get('eventIdList')

    if not event_id_list:
        return jsonify({'isSuccessful': False}), 400
    
    try:
        each_event_is_deleted = defaultdict(bool)
        for event_id in event_id_list:
            is_deleted = delete_event_service(user_id, event_id)
            each_event_is_deleted[event_id] = is_deleted

        return jsonify(dict(**{'isSuccessful': True}, **each_event_is_deleted)), 200
    
    except Exception as e:
        main.logger.error(f"Error in delete_event: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    
@main.route('/users/<string:user_id>/events/<string:event_id>/members', methods=['POST'])
def create_members(user_id, event_id):
    data = request.json
    
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    member_name = data.get('newMemberName')

    if not member_name:
        return jsonify({'isSuccessful': False}), 400
    
    try:
        member_info = create_member_service(user_id, event_id, member_name)
        return jsonify(dict(**{'isSuccessful': True}, **member_info)), 201
    
    except Exception as e:
        main.logger.error(f"Error in create_members: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    
@main.route('/users/<string:user_id>/events/<string:event_id>/members/<string:member_id>', methods=['GET'])
def get_member(user_id, event_id, member_id):
    member = get_member_service(user_id, event_id, member_id)
    if member:
        return jsonify(dict(**{'isSuccessful': True}, **member)), 200
    else:
        return jsonify({'isSuccessful': False}), 404
    

@main.route('/users/<string:user_id>/events/<string:event_id>/members', methods=['DELETE'])
def delete_members(user_id, event_id):
    data = request.json

    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    member_id_list = data.get('memberIdList')

    if not member_id_list:
        return jsonify({'isSuccessful': False}), 400
    
    try:
        each_member_is_deleted = defaultdict(bool)
        for member_id in member_id_list:
            is_deleted = delete_member_service(user_id, event_id, member_id)
            each_member_is_deleted[member_id] = is_deleted

        return jsonify(dict(**{'isSuccessful': True}, **each_member_is_deleted)), 200
    
    except Exception as e:
        main.logger.error(f"Error in delete_members: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    

@main.route('/users/<string:user_id>/events/<string:event_id>/members/<string:member_id>', methods=['PUT'])
def edit_member_name(user_id, event_id, member_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    member_name = data.get('newMemberName')

    if not member_name:
        return jsonify({'isSuccessful': False}), 400
    
    member = update_member_service(user_id, event_id, member_id, member_name)

    return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 200

@main.route('/users/<string:user_id>/events/<string:event_id>/members/<string:member_id>/status', methods=['PUT'])
def change_member_status(user_id, event_id, member_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    status = data.get('status')

    if not status:
        return jsonify({'isSuccessful': False}), 400
    
    member = change_member_status_service(user_id, event_id, member_id, status)

    if not member:
        return jsonify({'isSuccessful': False}), 400

    return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 200
