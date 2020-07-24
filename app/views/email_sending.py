from flask_restful import Resource, reqparse

from app.tasks.tasks import send_async_email


parser = reqparse.RequestParser()
parser.add_argument('email_to_send_to',
                    help='Email to write to is required',
                    required=True)


class CeleryEmailSender(Resource):
    """Resource that sends emails."""

    def post(self):
        data = parser.parse_args()
        # send the email
        email_data = {
            'subject': 'Hello from Flask',
            'to': data['email_to_send_to'],
            'body': 'This is a test email sent from a background Celery task.'
        }
        send_async_email.apply_async(args=[email_data])
        return {
            "message": "Email to {0} was sent."
            .format(data['email_to_send_to'])
        }
