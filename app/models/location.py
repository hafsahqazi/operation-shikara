from datetime import datetime

from app import db


class Location(db.Model):
    __tablename__ = 'location'

    location_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user_phone_number = db.Column(db.String, db.ForeignKey('user.phone_number'))
    user = db.relationship('User')
