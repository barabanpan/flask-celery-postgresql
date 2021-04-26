Small apllication that requires postgresql, celery and redis.
Uses JWT tokens, uses db migrations via alembic and can send emails async because of celery:)

Uses gunicorn for WSGI support,
and WhiteNoise for static file serving.

# Prerequisites:
1. In root folder create config.py:
```
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'your-secret-key'

    JWT_SECRET_KEY = 'your-jwt-secret-key'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_DATABASE_URL = \
        "postgres://abc:your_pass@localhost:5432/db_name"

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
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
```
# Run:

1. Run like this (you'll need different tabs):
`sudo service redis-server start`
`celery -A celery_worker.celery worker [-l=DEBUG]`
`gunicorn --bind 0.0.0.0:5000 wsgi:app`

2. To play run Postman requests.

3. Don't forget to stop redis afterwards (just to be neat):
`sudo service redis-server stop`
