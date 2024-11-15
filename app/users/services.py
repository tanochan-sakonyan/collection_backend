from .models import User
from app import db

def create_user_service(line_token : str) -> User:
    user = User(line_token)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_service(user_id: int) -> User:
    return User.query.get(user_id)

def delete_user_service(user_id: int) -> None:
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def register_paypay_url_service(user_id: int, paypay_url: str) -> User:
    user = User.query.get(user_id)
    if not user:
        return None
    user.paypay_url = paypay_url
    db.session.commit()
    return user