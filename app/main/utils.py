from app import db

def get_user(user_id: str):
    doc_ref = db.collection('users').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None

def get_event(user_id: str, event_id: str):
    if not user_id or not event_id:
        return None

    query = db.collection('users').document(user_id).collection('events').document(event_id).stream()
    for event in query:
        return event.to_dict()

    return None

def get_events(user_id: str):
    events = []
    event_ref = db.collection('users').document(user_id).collection('events').stream()
    for event in event_ref:
        events.append(event.to_dict())
    return events

def get_members(user_id: str, event_id: str):
    members = []
    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').stream()
    for member in member_ref:
        members.append(member.to_dict())
    return members

def get_all_user_info(user_id: str):
    user = get_user(user_id)
    if not user:
        return None

    user['events'] = get_events(user_id)
    for event in user['events']:
        event['members'] = get_members(user_id, event['eventId'])

    return user

def get_all_event_info(event_id: str):
    event = get_event(event_id)
    if not event:
        return None

    event['members'] = get_members(event_id)
    return event