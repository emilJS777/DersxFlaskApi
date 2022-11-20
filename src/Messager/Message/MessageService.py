from src.__Parents.Service import Service
from .IMessageRepo import IMessageRepo
from flask import g
from ...__Parents.Repository import Repository


class MessageService(Service, Repository):

    def __init__(self, message_repository: IMessageRepo):
        self.message_repository: IMessageRepo = message_repository

    def create(self, body: dict) -> dict:
        self.message_repository.create(body)
        return self.response_created('сообщение отправленно')

    def update(self, message_id: int, body: dict) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message or not message.creator_id == g.user_id:
            return self.response_not_found('сообщение не найдено')
        self.message_repository.update(message=message, body=body)
        return self.response_updated('сообщение обновлено')

    def delete(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message or not message.creator_id == g.user_id:
            return self.response_not_found('сообщение не найдено')

        self.message_repository.delete(message=message)
        return self.response_updated('сообщение удалено')

    def get_by_id(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found('сообщение не найдено')
        return self.response_ok(self.get_dict_items(message))

    def get_all(self, limit: int, offset: int, room_id: int) -> dict:
        messages: list = self.message_repository.get_all(limit=limit, offset=offset, room_id=room_id)
        return self.response_ok([{
            'id': message.id,
            'text': message.text,
            'creator_id': message.creator_id,
            'creation_date': message.creation_date
        } for message in messages])
