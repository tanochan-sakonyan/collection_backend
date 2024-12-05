from app.users.models import User
from app import db
from .models import Member, Status

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

def edit_member_name_service(member_id: int, member_name: str) -> Member:
    member = Member.query.get(member_id)
    member.member_name = member_name
    db.session.commit()
    return member

def change_member_status_service(member_id: int, status: int) -> Member:
    #状態を表す数は0から2のみ
    if status not in [1, 2, 3]:
        return None
    
    member = Member.query.get(member_id)
    member.status = Status(status)
    db.session.commit()
    return member