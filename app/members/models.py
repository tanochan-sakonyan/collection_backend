from app import db
from enum import Enum

class Status(Enum):
    UNPAID = 0
    PAID = 1
    ABSENCE = 2

class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(64), index=True, nullable=False)
    line_user_id = db.Column(db.String(64), index=True, nullable=True, default=None)
    status = db.Column(db.Enum(Status), default=Status.UNPAID, nullable=False)
    # 外部キーを追加
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    event = db.relationship('Event', back_populates='members')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __init__(self, member_name, event_id):
        self.member_name = member_name
        self.event_id = event_id

    def to_dict(self):
        return {
            'event_id': self.event_id,
            'member_id': self.member_id,
            'member_name': self.member_name,
            'line_user_id': self.line_user_id,
            'status': self.status.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Member(member_id={self.member_id}, member_name='{self.member_name}')>"

    
