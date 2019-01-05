import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    LOCAL = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://postgres@localhost/qazimusab')


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    LOCAL = False


class StageConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOCAL = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOCAL = True


class DemoConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOCAL = False
