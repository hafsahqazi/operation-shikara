import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
# cors = CORS(app)


def create_app():
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['CORS_HEADERS'] = 'Content-Type'
    db.init_app(app)
    return app
