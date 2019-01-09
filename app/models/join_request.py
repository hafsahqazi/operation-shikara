from datetime import datetime

from app import db


class JoinRequest(db.Model):
    __tablename__ = 'join_request'

    accepted = db.Column(db.Boolean, nullable=False)
    requestorPhoneNum = db.Column(db.String, db.ForeignKey('user.phone_number'), primary_key=True)
    requesteePhoneNum = db.Column(db.String, db.ForeignKey('user.phone_number'), primary_key=True)
    sent_at = db.Column(db.DateTime, nullable= False, default=datetime.utcnow())

    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)
    group = db.relationship('Group')
