from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from whitenoise import WhiteNoise
from flask_migrate import Migrate

from .models.database import db, base
from .views import users_bp, add_users_routes


migrate = Migrate()
jwt = JWTManager()


def setup_database(app):
    with app.app_context():  # WHAT IS THAT FOR???
        @app.before_first_request
        def create_tables():
            base.metadata.create_all(db)

    migrate.init_app(app, db)


def setup_jwt(app):
    jwt.init_app(app)

    # CAN THIS BE MOVED TO revoked_token_model?
    # WHEN SHOULD IT BE DECORATED AND WHEN IT WILL BE
    # IF IN revoked_token_model?
    from .models.revoked_token_model import RevokedTokenModel

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return RevokedTokenModel.is_jti_blacklisted(jti)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.wsgi_app = WhiteNoise(app.wsgi_app, root='app/static/')

    @app.route('/')
    def index():
        return jsonify({"message": "Hello, World!"})

    # not happening in main because app is imported to wsgi
    setup_database(app)
    setup_jwt(app)

    # adding resources. Do that AFTER setup_database()
    add_users_routes()  # creates it's own api and adds it there
    app.register_blueprint(users_bp)  # blueprint connects that api and app

    return app
