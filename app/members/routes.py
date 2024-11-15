from flask import Blueprint, request, jsonify
from . import members_bp

from .services import create_member_service, get_member_service, delete_member_service

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