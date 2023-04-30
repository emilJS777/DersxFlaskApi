from src.__Parents.Controller import Controller
from .EmailService import EmailService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask import g
from .EmailSender import EmailSender
from .EmailRepository import EmailRepository


class EmailController(Controller):
    email_service: EmailService = EmailService(EmailRepository(), EmailSender())

    @AuthMiddleware.check_authorize
    def get(self):
        if self.arguments.get('activation_code'):
            random_code = self.email_service.generate_random_code()
            res = self.email_service.send_email_activation(code=random_code, email_address=g.user.email.address)
            return res

        if self.arguments.get('code'):
            res = self.email_service.email_activation(code=self.arguments.get('code'))
            return res
        else:
            return self.email_service.response_not_found('запрос неверный')