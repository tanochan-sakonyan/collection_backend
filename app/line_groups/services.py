from .models import LineGroup, LineUser
from .util import add_all_line_users_in_line_group_to_event
from app.events.models import Event
from app.members.models import Member
from app import db


def create_line_group_service(line_group_id: str, line_group_name: str) -> LineGroup:
    line_group = LineGroup(line_group_id, line_group_name)
    db.session.add(line_group)
    db.session.commit()
    return line_group

def get_line_group_service(line_group_id: str) -> LineGroup:
    return LineGroup.query.filter_by(line_group_id=line_group_id).first()

def delete_line_group_service(line_group_id: str) -> None:
    line_group = LineGroup.query.filter_by(line_group_id=line_group_id).first()
    if not line_group:
        return False
    db.session.delete(line_group)
    db.session.commit()
    return True

def create_line_user_service(line_user_id: str, line_user_name: str, line_group_id: int) -> LineUser:
    line_user = LineUser(line_user_id, line_user_name, line_group_id)
    db.session.add(line_user)
    db.session.commit()
    return line_user


def get_line_user_service(line_user_id: str) -> LineUser:
    return LineUser.query.filter_by(line_user_id=line_user_id).first()

def delete_line_user_service(line_user_id: str) -> None:
    line_user = LineUser.query.filter_by(line_user_id=line_user_id).first()
    if not line_user:
        return False
    db.session.delete(line_user)
    db.session.commit()
    return True

def create_event_from_line_group_service(user_id: int, line_group_id: str, event_name: str) -> Event:
    line_group = LineGroup.query.filter_by(line_group_id=line_group_id).first()
    if not line_group:
        return None
    
    event = Event(event_name, user_id, line_group.id)

    add_all_line_users_in_line_group_to_event(line_group, event)

    db.session.add(event)
    db.session.commit()

    return event

def add_members_in_line_group_to_existing_event_service(line_group_id: str, event_id: int) -> Event:
    line_group = LineGroup.query.filter_by(line_group_id=line_group_id).first()
    if not line_group:
        return None
    
    event = Event.query.get(event_id)
    if not event:
        return None

    add_all_line_users_in_line_group_to_event(line_group, event)

    db.session.commit()

    return event
