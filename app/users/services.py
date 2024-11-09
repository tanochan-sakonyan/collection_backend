from .models import User
from app import db

def create_user_service(email: str, password: str) -> User:
    user = User(email)
    user.set_password(password)
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