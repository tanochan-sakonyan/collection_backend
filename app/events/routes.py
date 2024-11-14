from flask import jsonify, request
from . import events_bp
from .services import create_event_service, get_event_service, delete_event_service, rename_event_service

@events_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@events_bp.route('/events', methods=['POST'])
def create_event():
    data = request.json

    if not data:
        return jsonify({'message': 'Data is required'}), 400
    
    event_name = data.get('eventName')
    user_id = data.get('userId')

    if not event_name or not user_id:
        return jsonify({'message': 'Event name and user ID are required'}), 400
    
    event = create_event_service(event_name, user_id)

    return jsonify(event.to_dict()), 201

@events_bp.route('/users/<int:user_id>/events/<int:event_id>', methods=['GET'])
def get_event(user_id, event_id):
    event = get_event_service(event_id)
    if event:
        return jsonify(event.to_dict()), 200
    else:
        return jsonify({'message': 'Event not found'}), 404

@events_bp.route('/users/<int:user_id>/events/<int:event_id>', methods=['DELETE'])
def delete_event(user_id, event_id):
    Is_deleted = delete_event_service(event_id)
    if Is_deleted:
        return jsonify({'message': 'Event deleted'}), 200
    else:
        return jsonify({'message': 'Event not found'}), 404
    
@events_bp.route('/users/<int:user_id>/events/<int:event_id>', methods=['PUT'])
def rename_event(user_id, event_id):
    data = request.json

    if not data:
        return jsonify({'message': 'Data is required'}), 400
    
    event_name = data.get('event_name')

    if not event_name:
        return jsonify({'message': 'Event name is required'}), 400
    
    event = rename_event_service(event_id, event_name)

    return jsonify(event.to_dict()), 200
    

    

    