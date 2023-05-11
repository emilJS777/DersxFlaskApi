from .IUserContactRepo import IUserContactRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class UserContactService(Service, Repository):
    def __init__(self, user_contact_repository: IUserContactRepo):
        self.user_contact_repository: IUserContactRepo = user_contact_repository

    def create(self, body: dict) -> dict:
        self.user_contact_repository.create(body)
        return self.response_created(msg_rus='контактная информация создана',
                                     msg_eng='contact information created',
                                     msg_arm='կոնտակտային տվյալները ստեղծված են')

    def update(self, user_contact_id: int, body: dict) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found(msg_rus='контактная информация не найдена',
                                           msg_arm='կոնտակտային տվյալները չեն գտնվել',
                                           msg_eng='contact information not found')
        self.user_contact_repository.update(user_contact, body)
        return self.response_updated(msg_rus='контактная информация обновлена',
                                     msg_eng='contact information updated',
                                     msg_arm='կոնտակտային տվյալները թարմացվել են')

    def delete(self, user_contact_id: int) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found(msg_rus='контактная информация не найдена',
                                           msg_arm='կոնտակտային տվյալները չեն գտնվել',
                                           msg_eng='contact information not found')
        self.user_contact_repository.delete(user_contact)
        return self.response_deleted(msg_rus='контактная информация удалена',
                                     msg_arm='կոնտակտային տվյալները հեռացվել են',
                                     msg_eng='contact information removed')

    def get_by_id(self, user_contact_id: int) -> dict:
        user_contact = self.user_contact_repository.get_by_id(user_contact_id)
        if not user_contact or not user_contact.user_id == g.user_id:
            return self.response_not_found(msg_rus='контактная информация не найдена',
                                           msg_arm='կոնտակտային տվյալները չեն գտնվել',
                                           msg_eng='contact information not found')
        return self.response_ok(self.get_dict_items(user_contact))

    def get_all(self, user_id: int) -> dict:
        user_contacts = self.user_contact_repository.get_all(user_id)
        return self.response_ok(self.get_array_items(user_contacts))
