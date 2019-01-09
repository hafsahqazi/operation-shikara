import json

from flask import abort, request, url_for, jsonify
from app import db
from . import unauthorized
from ..models import *


@unauthorized.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify({"Users": [user.as_dict() for user in users]})


@unauthorized.route('/users', methods=['POST'])
def register_user():
    first_name = request.json.get('FirstName')
    last_name = request.json.get('LastName')
    phone_number = request.json.get('PhoneNumber')
    email = request.json.get('Email')
    username = request.json.get('Username')
    user = User(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        username=username
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.as_dict()), 201
