from flask.blueprints import Blueprint
from flask_restful import Api

from .users import (UserRegistration, UserLogin, UserLogoutAccess,
    UserLogoutRefresh, TokenRefresh, AllUsers, SecretResource
)
from .email_sending import CeleryEmailSender

users_bp = Blueprint('users', __name__)
email_sender_bp = Blueprint('emails', __name__)


def add_users_routes():
    api = Api(users_bp)

    api.add_resource(UserRegistration, '/registration')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogoutAccess, '/logout/access')
    api.add_resource(UserLogoutRefresh, '/logout/refresh')
    api.add_resource(TokenRefresh, '/token/refresh')
    api.add_resource(AllUsers, '/users')
    api.add_resource(SecretResource, '/secret')


def add_emails_routes():
    api = Api(email_sender_bp)

    api.add_resource(CeleryEmailSender, '/emails')
