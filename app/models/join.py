from datetime import datetime

from app import db


class Join(db.Model):
    __tablename__ = 'join'

    joined_at= db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow())

    user_phone_number = db.Column(db.String, db.ForeignKey('user.phone_number'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)

    user = db.relationship("User", back_populates="groups")
    group = db.relationship("Group", back_populates="users")