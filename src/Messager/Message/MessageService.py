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
            'room_id': message.room_id,
            'creation_date': str(message.creation_date)
        }

        self.socketio.send(emit_name='message', data=body_mess, user_id=body['user_id'])
        return self.response_ok(body_mess)

    def update(self, message_id: int, body: dict) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message or not message.creator_id == g.user_id:
            return self.response_not_found(msg_rus='сообщение не найдено',
                                           msg_eng='message not found',
                                           msg_arm='հաղորդագրությունը չի գտնվել')
        new_message = self.message_repository.update(message=message, body=body)
        new_mess_body: dict = {
            'id': new_message.id,
            'text': new_message.text,
            'read': new_message.read,
            'edited': new_message.edited,
            'room_id': new_message.room_id,
            'creator_id': new_message.creator_id,
            'creation_date': str(message.creation_date)
        }
        self.socketio.send(emit_name='message_update', data=new_mess_body, user_id=new_message.addresser_id)
        return self.response_updated(msg_rus='сообщение обновлено',
                                     msg_arm='հաղորդագրությունը թարմացված է',
                                     msg_eng='message updated')

    def read(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found(msg_rus='сообщение не найдено',
                                           msg_eng='message not found',
                                           msg_arm='հաղորդագրությունը չի գտնվել')
        self.message_repository.read(message)
        self.socketio.send(emit_name='message_read', data={'message_id': message_id, 'room_id': message.room_id}, user_id=message.creator_id)
        return self.response_updated(msg_eng='read', msg_rus='', msg_arm='')

    def delete(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message or not message.creator_id == g.user_id:
            return self.response_not_found(msg_rus='сообщение не найдено',
                                           msg_eng='message not found',
                                           msg_arm='հաղորդագրությունը չի գտնվել')

        self.message_repository.delete(message=message)
        self.socketio.send(emit_name='message_delete', data={'id': message.id, 'room_id': message.room_id}, user_id=message.addresser_id)
        return self.response_deleted(msg_rus='сообщение удалено',
                                     msg_arm='հաղորդագրությունը ջնջված է',
                                     msg_eng='message deleted')

    def get_by_id(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found(msg_rus='сообщение не найдено',
                                           msg_eng='message not found',
                                           msg_arm='հաղորդագրությունը չի գտնվել')
        return self.response_ok(self.get_dict_items(message))

    def get_all(self, limit: int, offset: int, room_id: int) -> dict:
        messages: list = self.message_repository.get_all(limit=limit, offset=offset, room_id=room_id)
        return self.response_ok([{
            'id': message.id,
            'text': message.text,
            'read': message.read,
            'edited': message.edited,
            'creator_id': message.creator_id,
            'creation_date': message.creation_date
        } for message in messages])

    def get_not_read(self) -> dict:
        messages: list = self.message_repository.get_not_read()
        return self.response_ok([{
            'id': message.id,
            'text': message.text,
            'read': message.read,
            'edited': message.edited,
            'room_id': message.room_id,
            'creator_id': message.creator_id,
            'creation_date': message.creation_date
        } for message in messages])
