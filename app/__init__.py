import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
cors = CORS(app)


def create_app():
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['CORS_HEADERS'] = 'Content-Type'
    db.init_app(app)
        # register blueprints
    from .authorized import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .unauthorized import unauthorized as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api')
    return app
