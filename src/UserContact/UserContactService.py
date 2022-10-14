from .IUserContactRepo import IUserContactRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class UserContactService(Service, Repository):
    def __init__(self, user_contact_repository: IUserContactRepo):
        self.user_contact_repository: IUserContactRepo = user_contact_repository

    def create(self, body: dict) -> dict:
        self.user_contact_repository.create(body)
        return self.response_created('контактная информация создана')

    def update(self, user_contact_id: int, body: dict) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found('контактная информация не найдена')
        self.user_contact_repository.update(user_contact, body)
        return self.response_updated('контактная информация обновлена')

    def delete(self, user_contact_id: int) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found('контактная информация не найдена')
        self.user_contact_repository.delete(user_contact)
        return self.response_deleted('контактная информация удалена')

    def get_by_id(self, user_contact_id: int) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found('контактная информация не найдена')
        return self.response_ok(self.get_dict_items(user_contact))

    def get_all(self, user_id: int) -> dict:
        user_contacts = self.user_contact_repository.get_all(user_id)
        return self.response_ok(self.get_array_items(user_contacts))
