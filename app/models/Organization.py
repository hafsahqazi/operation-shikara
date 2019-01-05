from app import db


class Organization(db.Model):
    __tablename__ = 'organization'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
