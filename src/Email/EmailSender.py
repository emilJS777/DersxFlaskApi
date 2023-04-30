from .IEmailSender import IEmailSender
from email.mime.text import MIMEText
from src import app
import smtplib, ssl


class EmailSender(IEmailSender):
    def send(self, addresses, header, html):
        message = MIMEText(html, 'html', 'utf-8')
        message['Subject'] = header
        message['From'] = app.config['MAIL_USERNAME']
        message['To'] = ', '.join(addresses)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(app.config['MAIL_SERVER'], app.config['MAIL_PORT'], context=context) as server:
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.sendmail(app.config['MAIL_USERNAME'], addresses, message.as_string())