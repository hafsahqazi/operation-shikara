#!/usr/bin/env python

from app import create_app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
from app.models import Organization
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
