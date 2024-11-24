from app import db

class LineGroup(db.Model):
    __tablename__ = 'line_groups'
    id = db.Column(db.Integer, primary_key=True)
    line_group_id = db.Column(db.String(64), index=True, nullable=False)
    line_group_name = db.Column(db.String(64), index=True, nullable=False)
    line_users_in_group = db.relationship('LineUser', back_populates='line_group', lazy='select', cascade="all, delete  orphan")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __init__(self, line_group_id, line_group_name):
        self.line_group_id = line_group_id
        self.line_group_name = line_group_name
    
    def to_dict(self):
        return {
            'id': self.id,
            'line_group_id': self.line_group_id,
            'line_group_name': self.line_group_name,
            'line_users_in_group': [line_user.to_dict() for line_user in self.line_users_in_group],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }



class LineUser(db.Model):
    __tablename__ = 'line_users'

    id = db.Column(db.Integer, primary_key=True)    
    line_user_id = db.Column(db.String(64), index=True, nullable=False)
    line_user_name = db.Column(db.String(64), index=True, nullable=False)

    line_group_id = db.Column(db.Integer, db.ForeignKey('line_groups.id'), nullable=False)
    line_group = db.relationship('LineGroup', back_populates='line_users_in_group')

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __init__(self, line_user_id, line_user_name, line_group_id):
        self.line_user_id = line_user_id
        self.line_user_name = line_user_name
        self.line_group_id = line_group_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'line_user_id': self.line_user_id,
            'line_user_name': self.line_user_name,
            'line_group_id': self.line_group_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

