class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aaa'

    JWT_SECRET_KEY = 'your-jwt-secret-key'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_DATABASE_URL = \
        "postgres://abc:your_pass@localhost:5432/db_name"

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465 #587
    MAIL_USE_SSL = True

    MAIL_USERNAME = 'your_email@example.com'
    MAIL_PASSWORD = 'your_pass'
    MAIL_DEFAULT_SENDER = 'flask@example.com'


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
