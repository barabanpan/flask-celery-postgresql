Has NO cyclic imports! 
Application Factory pattern was used to avoid it.
(You can see how pretty run.py is now)

Runs like this:
FLASK_APP=run.py FLASK_DEBUG=1 flask run
(runs even with cyclic imports)

And like this:
python run.py

Uses postgreSQL, use cmd to select tables.

You better have config files outside your app package.
Config.py is imported in run.apy create_app()

Uses gunicorn for ...?
and WhiteNoise for static file serving.
