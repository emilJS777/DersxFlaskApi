from src.__Parents.Service import Service
from .EmailHtml import EmailHtml
from flask import g
from .IEmaiRepo import IEmailRepo
from .IEmailSender import IEmailSender


class EmailService(Service):

    def __init__(self, email_repository: IEmailRepo, email_sender: IEmailSender):
        self.email_repository: IEmailRepo = email_repository
        self.email_sender: IEmailSender = email_sender

    def send_email_activation(self, code, email_address):
        try:
            self.email_sender.send(addresses=[email_address], header='подтверждения эл. почты', html=EmailHtml.email_activation(code))
            self.email_repository.update_activation_code(code=code)
            return self.response_created(f'письмо для подтверждения эл почты отправленно по {email_address}')
        except:
            return self.response_not_found('адрес эл. почты не найден, пожалуйста пропишите существующую эл.почту ')

    def email_activation(self, code):
        if g.user.email.active:
            return self.response_conflict('ваш адрес электронной почты уже подтвежден ')
        if g.user.email.activation_code == code:
            self.email_repository.create_activation()
            return self.response_updated('адрес электронной почты успешно подтвержден')
        else:
            return self.response_not_found('код активации неверный')

