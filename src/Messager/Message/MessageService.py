from src.__Parents.Service import Service
from .IMessageRepo import IMessageRepo
from flask import g
from ...Socketio.ISocketio import ISocketio
from ...__Parents.Repository import Repository


class MessageService(Service, Repository):

    def __init__(self, message_repository: IMessageRepo, socketio: ISocketio):
        self.message_repository: IMessageRepo = message_repository
        self.socketio = socketio

    def create(self, body: dict) -> dict:
        message = self.message_repository.create(body)
        body_mess: dict = {
            'id': message.id,
            'text': message.text,
            'read': message.read,
            'creator_id': message.creator_id,
            'room_id': message.room_id
        }

        self.socketio.send(emit_name='message', data=body_mess, user_id=body['user_id'])
        return self.response_ok(body_mess)

    def update(self, message_id: int, body: dict) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message or not message.creator_id == g.user_id:
            return self.response_not_found('сообщение не найдено')
        self.message_repository.update(message=message, body=body)
        return self.response_updated('сообщение обновлено')

    def read(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found('сообщение не найдено')
        self.message_repository.read(message)
        self.socketio.send(emit_name='message_read', data={'message_id': message_id, 'room_id': message.room_id}, user_id=message.creator_id)
        return self.response_updated('read')

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
            'read': message.read,
            'creator_id': message.creator_id,
            'creation_date': message.creation_date
        } for message in messages])

    def get_not_read(self) -> dict:
        messages: list = self.message_repository.get_not_read()
        return self.response_ok([{
            'id': message.id,
            'text': message.text,
            'read': message.read,
            'room_id': message.room_id,
            'creator_id': message.creator_id,
            'creation_date': message.creation_date
        } for message in messages])
