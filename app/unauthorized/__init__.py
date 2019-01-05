from flask import Blueprint

unauthorized = Blueprint('unauthorized', __name__)
from . import unauthorized_calls