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
            self.email_sender.send(addresses=[email_address], header='email confirmation', html=EmailHtml.email_activation(code))
            self.email_repository.update_activation_code(code=code)
            return self.response_created(msg_rus=f'письмо для подтверждения эл почты отправленно по {email_address}',
                                         msg_eng=f'email confirmation email sent to {email_address}',
                                         msg_arm=f'{email_address}-ին ուղարկված է հաստատման նամակ ')
        except:
            return self.response_not_found(msg_rus='адрес эл. почты не найден, пожалуйста пропишите существующую эл.почту ',
                                           msg_eng='email address not found, please enter an existing email',
                                           msg_arm='էլ. փոստը չի գտնվել, խնդրում ենք մուտքագրել գոյություն ունեցող էլ. հասցէ')

    def email_activation(self, code):
        if g.user.email.active:
            return self.response_conflict(msg_rus='ваш адрес электронной почты уже подтвежден ',
                                          msg_arm='ձեր էլ. փոստի հասցեն արդեն ստուգված է',
                                          msg_eng='your email address has already been verified')
        if g.user.email.activation_code == code:
            self.email_repository.create_activation()
            return self.response_updated(msg_rus='адрес электронной почты успешно подтвержден',
                                         msg_eng='email address successfully verified',
                                         msg_arm='էլ. փոստի հասցեն հաջողությամբ հաստատվել է')
        else:
            return self.response_not_found(msg_rus='код активации неверный',
                                           msg_eng='activation code is invalid',
                                           msg_arm='ակտիվացման կոդը անվավեր է')

