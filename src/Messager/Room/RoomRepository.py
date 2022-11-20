from sqlalchemy import and_, or_
from .IRoomRepo import IRoomRepo
from .RoomModel import Room
from src.User.UserModel import User
from flask import g
from ..Message.MessageModel import Message


class RoomRepository(IRoomRepo):
    def create(self, users: list) -> Room:
        room: Room = Room()
        room.users = users
        room.save_db()
        return room

    def delete(self, room: Room):
        room.delete_db()

    def get_by_user_id(self, user_id: int) -> Room:
        room: Room = Room.query.where(Room.users.any(and_(User.id == user_id, User.id == g.user_id))).first()
        return room

    def get_all(self, limit: int, offset: int) -> list[Room]:
        room: list[Room] = Room.query.join(Room.message).order_by(-Message.creation_date).join(Room.users).where(User.id == g.user_id).all()
        return room
