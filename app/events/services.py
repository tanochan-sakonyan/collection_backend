from app.users.models import User
from app import db
from .models import Event

def create_event_service(event_name: str, user_id: int) -> Event:
    event = Event(event_name, user_id)
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

