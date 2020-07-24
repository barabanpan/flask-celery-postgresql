from flask_mail import Mail, Message
import time

from app import celery
from app import app  # mail stuff needs app_context


mail = Mail(app)

# bind needs self
@celery.task(bind=True)
def send_async_email(self, email_data):
    """Sends an email aafter 25 seconds."""
    with app.app_context():
        msg = Message(subject=email_data["subject"],
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[email_data['to']])
        msg.body = email_data['body']

        time.sleep(25)
        mail.send(msg)
