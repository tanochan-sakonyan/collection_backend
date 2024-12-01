from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .util import get_line_user_id

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    line_user_id = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    paypay_url = db.Column(db.String(128), default=None, nullable=True)
    events = db.relationship('Event', back_populates='user', lazy='select', cascade="all, delete-orphan")

    def __init__(self, line_token):
        self.line_user_id = get_line_user_id(line_token)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'paypay_url': self.paypay_url,
            'events': [event.to_dict() for event in self.events]
        }

    



