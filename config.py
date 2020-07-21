import os
basedir = os.path.abspath(os.path.dirname(__file__))
# ?


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True  # ?
    SECRET_KEY = 'aaa'
    #  not used yet
    SQLALCHEMY_DATABASE_URL = \
    "postgres://nataliia:nat_postgres_88@localhost:5432/nataliia"

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
