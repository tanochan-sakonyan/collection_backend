from app import db

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    members = db.relationship('Member', back_populates='event', lazy='select', cascade="all, delete-orphan")
    user = db.relationship('User', back_populates='events')
    line_group_id = db.Column(db.Integer, nullable=True)

    def __init__(self, event_name, user_id, line_group_id=None):
        self.event_name = event_name
        self.user_id = user_id
        if line_group_id:
            self.line_group_id = line_group_id

    def add_member(self, member):
        self.members.append(member)
        return member
    
    def remove_member(self, member):
        self.members.remove(member)
        return member
    
    def to_dict(self):
        return {
            'event_id': self.event_id,
            'event_name': self.event_name,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'members': [member.to_dict() for member in self.members]
        }
    
    