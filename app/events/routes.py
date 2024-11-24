from flask import jsonify, request
from . import events_bp
from .services import create_event_service, get_event_service, delete_event_service, rename_event_service, remind_payment_to_line_group_service
from collections import defaultdict

@events_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@events_bp.route('/events', methods=['POST', "DELETE"])
def create_event():
    if request.method == 'POST':
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Data is required'}), 400
    
        event_name = data.get('eventName')
        user_id = data.get('userId')

        if not event_name or not user_id:
            return jsonify({'message': 'Event name and user ID are required'}), 400
        
        event = create_event_service(event_name, user_id)

        return jsonify(event.to_dict()), 201

    if request.method == 'DELETE':
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Data is required'}), 400

        event_id_list = data.get('eventIdList')
        if not event_id_list:
            return jsonify({'message': 'Event ID is required'}), 400

        each_event_is_deleted = defaultdict(bool)

        for event_id in event_id_list:
            is_deleted = delete_event_service(event_id)#TODO:現状各eventに対して削除→DB反映を繰り返してるので、一括削除処理を実装する
            each_event_is_deleted[event_id] = is_deleted   

        return jsonify(each_event_is_deleted), 200


@events_bp.route('/events/<int:event_id>/reminders', methods=['POST'])
def remind_payment(event_id):
    message = remind_payment_to_line_group_service(event_id)

    if not message:
        return jsonify({"isSuccessful": False}), 400
    
    return jsonify({"isSuccessful": True, "message": message}), 200