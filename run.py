from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from models.database import db, base


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    @app.route('/')
    def index():
        return jsonify({"message": "Hello, World!"})

    return app


def setup_database(app):
    # 1. Do we need this line?
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():  # CAN WE DO THAT???
        @app.before_first_request
        def create_tables():
            base.metadata.create_all(db)


def setup_jwt(app):
    jwt = JWTManager(app)

    # 2. Shoudld this be in config as well?
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    # DO IT SOMEPLACE HIGHER???
    from models.revoked_token_model import RevokedTokenModel
    # WHERE SHOULD IT BE???

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return RevokedTokenModel.is_jti_blacklisted(jti)


# not happening in main because app is imported to wsgi
app = create_app()
setup_database(app)
setup_jwt(app)

# adding resources. Do that AFTER setup_database()
from views.manage_blueprints import users, add_users_routes
add_users_routes()  # creates it's own api and adds it there
app.register_blueprint(users)  # blueprint connects that api and app

# app.run()
