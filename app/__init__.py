from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from whitenoise import WhiteNoise
from flask_migrate import Migrate

from .models.database import db, base
from .views.manage_blueprints import users, add_users_routes


def setup_database(app):
    with app.app_context():  # CAN WE DO THAT???
        @app.before_first_request
        def create_tables():
            base.metadata.create_all(db)


def setup_jwt(app):
    jwt = JWTManager(app)

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
    app.register_blueprint(users)  # blueprint connects that api and app

    from .models.revoked_token_model import RevokedTokenModel
    from .models.user_model import UserModel

    migrate = Migrate(app, db)
    return app
