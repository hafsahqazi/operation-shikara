import json

from flask import abort, request, url_for
from app import db
from . import unauthorized
from ..models import Organization


@unauthorized.route('/organizations', methods=['POST'])
def add_organizations():
    """Creates a new Organization."""
    organization = Organization()
    db.session.add(organization)
    db.session.commit()
    return '', 204
