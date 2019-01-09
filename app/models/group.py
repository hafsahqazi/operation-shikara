from datetime import datetime

from app import db


class Group(db.Model):
    __tablename__ = 'group'

    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    # foreign key
    creator_phone_number=db.Column(db.String, db.ForeignKey('user.phone_number'))

    # for linking tables
    users = db.relationship("Join", back_populates = "group")

