from datetime import datetime

from app import db


class User(db.Model):
    __tablename__ = 'user'

    phone_number = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    groups = db.relationship("Join", back_populates= "user")

    def as_dict(self):
        return {
            'PhoneNumber': self.phone_number,
            'Name': self.first_name + ' ' + self.last_name
        }