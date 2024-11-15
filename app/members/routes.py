from flask import Blueprint, request, jsonify
from . import members_bp

from .services import create_member_service, get_member_service, delete_member_service, edit_member_name_service, change_member_status_service

@members_bp.route('/events/<int:event_id>/members', methods=['POST'])
def create_member(event_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    member_name = data.get('newMemberName')
    if not member_name:
        return jsonify({'isSuccessful': False}), 400
    member = create_member_service(member_name, event_id)

    return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 201

@members_bp.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = get_member_service(member_id)
    if member:
        return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 200
    else:
        return jsonify({'isSuccessful': False}), 404
    
@members_bp.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    is_deleted = delete_member_service(member_id)
    if is_deleted:
        return jsonify({'isSuccessful': True}), 200
    else:
        return jsonify({'isSuccessful': False}), 404
    
@members_bp.route('/members/<int:member_id>', methods=['PUT'])
def edit_member_name(member_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    member_name = data.get('newMemberName')

    if not member_name:
        return jsonify({'isSuccessful': False}), 400
    
    member = edit_member_name_service(member_id, member_name)

    return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 200

@members_bp.route('/members/<int:member_id>/status', methods=['PUT'])
def change_member_status(member_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    status = data.get('status')

    if not status:
        return jsonify({'isSuccessful': False}), 400
    
    member = change_member_status_service(member_id, status)

    if not member:
        return jsonify({'isSuccessful': False}), 400

    return jsonify(dict(**{'isSuccessful':True}, **member.to_dict())), 200
    
