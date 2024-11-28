from flask import Blueprint, request, jsonify
from . import line_groups_bp
from .services import create_event_from_line_group_service

@line_groups_bp.route('/users/<int:user_id>/events/line_groups', methods=['POST'])
def create_event_from_line_group(user_id):
    data = request.json
    if not data:
        return jsonify({'isSuccessful': False}), 400
    
    line_group_id = data.get('lineGroupId')
    line_group_name = data.get('lineGroupName')
    if not line_group_id or not line_group_name:
        return jsonify({'isSuccessful': False}), 400

    event = create_event_from_line_group_service(user_id, line_group_id, line_group_name)
    if not event:
        return jsonify({'isSuccessful': False}), 404
    
    return jsonify(dict(**{'isSuccessful':True}, **event.to_dict())), 201