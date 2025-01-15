from app import db
from google.cloud import firestore
from .utils import get_all_user_info, get_members, get_all_event_info

def register_paypay_url_service(user_id: str, paypay_url: str):
    if not user_id or not paypay_url:
        return None

    user_ref = db.collection('users').document(user_id)
    user_ref.update({
        'paypay_url': paypay_url
    })

    return get_all_user_info(user_id)

def create_event_service(user_id: str, event_name: str):
    if not user_id or not event_name:
        return None

    event_ref = db.collection('users').document(user_id).collection('events').document()
    event_ref.set({
        'event_id': event_ref.id,
        'event_name': event_name,
        'created_at': db.SERVER_TIMESTAMP
    })

    return get_all_event_info(user_id, event_ref.id)

def get_event_service(user_id: str, event_id: str):
    if not event_id:
        return None

    return get_all_event_info(user_id, event_id)

def update_event_service(user_id: str, event_id: str, event_name: str):
    if not user_id or not event_id or not event_name:
        return None

    event_ref = db.collection('users').document(user_id).collection('events').document(event_id)
    event_ref.update({
        'event_name': event_name
    })

    return get_all_event_info(user_id, event_id)

def delete_event_service(user_id: str, event_id: str):
    if not user_id or not event_id:
        return None

    event_ref = db.collection('users').document(user_id).collection('events').document(event_id).stream()  
    event_ref.delete()

    return None

def create_member_service(user_id: str, event_id: str, member_name: str):
    if not user_id or not event_id or not member_name:
        return None

    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').document()
    member_ref.set({
        'member_id': member_ref.id,
        'member_name': member_name,
        'created_at': firestore.SERVER_TIMESTAMP,
        'status': 2
    })

    member = member_ref.get()

    return member.to_dict()

def get_member_service(user_id: str, event_id: str, member_id: str):
    if not user_id or not event_id or not member_id:
        return None

    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').document(member_id)
    member = member_ref.get()

    return member.to_dict()
    

def update_member_service(user_id: str, event_id: str, member_id: str, member_name: str):
    if not user_id or not event_id or not member_id or not member_name:
        return None

    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').document(member_id)
    member_ref.update({
        'member_name': member_name
    })

    member = member_ref.get()

    return member.to_dict()

def delete_member_service(user_id: str, event_id: str, member_id: str):
    if not user_id or not event_id or not member_id:
        return None

    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').document(member_id)
    member_ref.delete()

    return None

def get_members_service(user_id: str, event_id: str):
    if not user_id or not event_id:
        return None
    
    return get_members(user_id, event_id)   

def change_member_status_service(user_id: str, event_id: str, member_id: str, status: int):
    if not user_id or not event_id or not member_id or not status:
        return None

    member_ref = db.collection('users').document(user_id).collection('events').document(event_id).collection('members').document(member_id)
    member_ref.update({
        'status': status
    })

    member = member_ref.get()

    return member.to_dict()



