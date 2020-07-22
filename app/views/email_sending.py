from flask_restful import Resource, reqparse
from flask_mail import Message
from flask import current_app

# also app to get configs
# HOW THE FUCK CONFIGS WORK AND HOW SHOULD I GET THINGS FROM THEM?
from app import mail, celery  # REALLY HOPE IT WORKS


@celery.task
def send_async_email(email_data):
    msg = Message(subject=email_data["subject"],
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    with current_app.app_context():
        mail.send(msg)
    # return ?


parser = reqparse.RequestParser()
parser.add_argument('email_to_send_to',
                    help='Email to write to is required',
                    required=True)
parser.add_argument('delay',
                    help='Time in seconds to wait before sending. Def = 0',
                    type=int,
                    default=0)


class CeleryEmailSender(Resource):
    """Resource for adding a new user (registration)."""

    def post(self):
        data = parser.parse_args()
        # send the email
        email_data = {
            'subject': 'Hello from Flask',
            'to': data['email_to_send_to'],
            'body': 'This is a test email sent from a background Celery task.'
        }
        send_async_email(email_data)
        if data['delay'] == 0:
            # send right away
            send_async_email.apply_async(args=[email_data])
            return {
                "message": "Email to {0} was sent."
                .format(data['email_to_send_to'])
            }
        else:
            # send with a delay
            send_async_email.apply_async(args=[email_data],
                                         countdown=email_data["delay"])
            return {
                "message": "Email to {0} will be sent in {1} s."
                .format(data['email_to_send_to'], data['delay'])
            }
