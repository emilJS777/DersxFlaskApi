from .IMessageRepo import IMessageRepo
from .MessageModel import Message
from flask import g


class MessageRepository(IMessageRepo):
    def create(self, body: dict):
        message: Message = Message()
        message.room_id = body['room_id']
        message.creator_id = g.user_id
        message.text = body['text']
        message.save_db()

    def update(self, message: Message, body: dict):
        message.text = body['text']
        message.update_db()

    def delete(self, message: Message):
        message.delete_db()

    def get_by_id(self, message_id: int) -> Message:
        message: Message = Message.query.filter_by(id=message_id).first()
        return message

    def get_all(self, limit: int, offset: int, room_id: int) -> list[Message]:
        messages: list[Message] = Message.query.filter_by(room_id=room_id).order_by(-Message.creation_date).limit(limit).offset(offset)
        return messages
