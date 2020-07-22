import os
basedir = os.path.abspath(os.path.dirname(__file__))
# ?


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True  # ?
    SECRET_KEY = 'aaa'

    JWT_SECRET_KEY = 'jwt-secret-key'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    #  not used yet
    SQLALCHEMY_DATABASE_URL = \
    "postgres://nataliia:nat_postgres_88@localhost:5432/nataliia"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
