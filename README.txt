Small apllication that requires postgresql, celery and redis.
Uses JWT tokens, uses db migrations via alembic and can send emails async because of celery:)

Has NO cyclic imports! 
Application Factory pattern was used to avoid it.

Uses gunicorn for WSGI support,
and WhiteNoise for static file serving.


NOW run like this (you'll need different tabs):
sudo service redis-server start
celery -A celery_worker.celery worker [-l=DEBUG]
gunicorn --bind 0.0.0.0:5000 wsgi:app

To play run Postman requests.

Don't forget to stop redis afterwards (just to be neat):
sudo service redis-server stop

P.S.
You better have config files outside your app package.
Config.py is imported in run.py create_app()
This config.py is an example and requires your data for app to run.

FOR MORE INFO READ COMMIT MESSAGES:)
