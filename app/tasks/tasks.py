from flask_mail import Message
import time
from flask import current_app

from app import celery, mail


# bind needs self
@celery.task(bind=True)
def send_async_email(self, email_data):
    """Sends an email aafter 25 seconds."""
    app = current_app._get_current_object()
    msg = Message(subject=email_data["subject"],
                  sender=app.config['MAIL_DEFAULT_SENDER'],  # ??
                  recipients=[email_data['to']])
    msg.body = email_data['body']

    time.sleep(25)
    with app.app_context():
        mail.send(msg)
