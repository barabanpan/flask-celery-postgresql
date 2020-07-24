Has NO cyclic imports! 
Application Factory pattern was used to avoid it.
(You can see how pretty run.py is now)

Used to be run like this:
FLASK_APP=run.py FLASK_DEBUG=1 flask run
(runs even with cyclic imports)

And like this:
python run.py

Uses postgreSQL, use cmd to select tables.

You better have config files outside your app package.
Config.py is imported in run.py create_app()

Uses gunicorn for WSGI support,
and WhiteNoise for static file serving.

NOW run like this (you'll need different tabs):
sudo service redis-server start
celery -A celery_worker.celery worker [-l=DEBUG]
gunicorn --bind 0.0.0.0:5000 wsgi:app

To play run Postman requests.

Don't forget to stop redis afterwards (just to be neat):
sudo service redis-server stop
