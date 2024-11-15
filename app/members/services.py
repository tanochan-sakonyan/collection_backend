from app.users.models import User
from app import db
from .models import Member

def create_member_service(member_name: str, event_id: int) -> Member:
    member = Member(member_name, event_id)
    db.session.add(member)
    db.session.commit()
    return member

def get_member_service(member_id: int) -> Member:
    return Member.query.get(member_id)

def delete_member_service(member_id: int) -> None:
    member = Member.query.get(member_id)
    if not member:
        return False
    db.session.delete(member)
    db.session.commit()
    return True