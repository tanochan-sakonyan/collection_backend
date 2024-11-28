from app.users.models import User
from app import db, line_bot_api
from .models import Event
from .util import make_paypay_remind_message
from app.util import send_message

def create_event_service(event_name: str, user_id: int) -> Event:
    event = Event(event_name, user_id, line_group_id=None)
    db.session.add(event)
    db.session.commit()
    return event

def get_event_service(event_id: int) -> Event:
    return Event.query.get(event_id)

def delete_event_service(event_id: int) -> None:
    event = Event.query.get(event_id)
    if not event:
        return False
    db.session.delete(event)
    db.session.commit()
    return True

def rename_event_service(event_id: int, event_name: str) -> Event:
    event = Event.query.get(event_id)
    event.event_name = event_name
    db.session.commit()
    return event

def remind_payment_to_line_group_service(event_id: int) -> str:
    event = Event.query.get(event_id)
    user = event.user

    if not event or not event.line_group_id:
        return None
    
    message = make_paypay_remind_message(members = event.members, paypay_url = user.paypay_url)

    if not message:
        return None
    
    result = send_message(event.line_group_id, message) 

    if not result:
        return None
    
    return message

