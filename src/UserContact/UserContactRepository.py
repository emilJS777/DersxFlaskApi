from .IUserContactRepo import IUserContactRepo
from .UserContactModel import UserContact
from flask import g


class UserContactRepository(IUserContactRepo):
    def create(self, body: dict):
        user_contact: UserContact = UserContact()
        user_contact.type = body['type']
        user_contact.information = body['information']
        user_contact.user_id = g.user_id
        user_contact.save_db()

    def update(self, user_contact: UserContact, body: dict):
        user_contact.type = body['type']
        user_contact.information = body['information']
        user_contact.update_db()

    def delete(self, user_contact: UserContact):
        user_contact.delete_db()

    def get_by_id(self, user_contact_id: int) -> UserContact:
        user_contact: UserContact = UserContact.query.filter_by(id=user_contact_id).first()
        return user_contact

    def get_all(self, user_id) -> list[UserContact]:
        user_contacts: list[UserContact] = UserContact.query.filter_by(user_id=user_id).all()
        return user_contacts
