from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'
    #ユーザー作成時に作られる情報
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column(db.String(512), nullable=False)  
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    #追加情報
    line_id    = db.Column(db.String(128), default=None, nullable=True)
    paypay_url = db.Column(db.String(128), default=None, nullable=True)
    events = db.relationship('Event', back_populates='user', lazy='select', cascade="all, delete-orphan")

    def __init__(self, email):
        self.email = email

    # パスワードのプロパティ
    @property
    def password(self) -> str:
        raise AttributeError('パスワードは読み取り不可です。')
    
    def set_password(self, plaintext_password: str) -> None:
        self._password = generate_password_hash(plaintext_password)

    def verify_password(self, plaintext_password: str) -> bool:
        return check_password_hash(self._password, plaintext_password)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'line_id': self.line_id,
            'paypay_url': self.paypay_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'events': [event.to_dict() for event in self.events]
        }

    def __repr__(self) -> str:
        return f"<User(user_id={self.user_id}, email='{self.email}')>"
    



