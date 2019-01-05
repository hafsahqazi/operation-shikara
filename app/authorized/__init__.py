from flask import Blueprint
# from ..unauthorized import auth_token
# from .authentication import auth_token
from flask.ext.cors import CORS

from app import db

api = Blueprint('api', __name__)

## Need to get/import app. here for autodoc

