from .IEmaiRepo import IEmailRepo
from flask import g
from .EmailModel import Email


class EmailRepository(IEmailRepo):

    def create(self, user_id: int, body: dict):
        email: Email = Email()
        email.user_id = user_id
        email.address = body['email_address']
        email.save_db()

    def update(self, email: Email, body: dict):
        if body.get('email_address'):
            if not email.address == body['email_address']:
                email.active = False
                email.address = body['email_address']
                email.update_db()

    def get_by_address(self, address: str):
        email = Email.query.filter(Email.address == address).first()
        return email

    def get_by_address_exclude_user_id(self, user_id: int, address: str):
        email = Email.query.filter(Email.user_id != user_id, Email.address == address).first()
        return email

    def create_activation(self):
        g.user.email.active = True
        g.user.email.activation_code = ''
        g.user.update_db()

    def update_activation_code(self, code):
        g.user.email.activation_code = code
        g.user.update_db()
