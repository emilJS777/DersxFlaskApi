from src.__Parents.Service import Service
from .IRoomRepo import IRoomRepo
from src.User.IUserRepo import IUserRepo
from flask import g
from ...__Parents.Repository import Repository


class RoomService(Service, Repository):
    def __init__(self, room_repository: IRoomRepo, user_repository: IUserRepo):
        self.room_repository: IRoomRepo = room_repository
        self.user_repository: IUserRepo = user_repository

    def delete(self, user_id: int) -> dict:
        room = self.room_repository.get_by_user_id(user_id)
        print(user_id)
        if not room:
            return self.response_not_found('рум не найден')
        self.room_repository.delete(room)
        return self.response_deleted('сообщения удалены')

    def get(self, user_id: int) -> dict:
        room = self.room_repository.get_by_user_id(user_id)

        if not room:
            users = self.user_repository.get_all_by_ids(user_ids=[user_id, g.user_id])
            room = self.room_repository.create(users=users)

        partner = room.users[0] if int(room.users[0].id) == int(user_id) else room.users[1]
        return self.response_ok({
            'id': room.id,
            'user': {
                'id': partner.id,
                'name': partner.name,
                'first_name': partner.first_name,
                'last_name': partner.last_name,
                'image': self.get_dict_items(partner.image) if partner.image else None
            }
        })

    def get_all(self, limit: int, offset: int, search: str) -> dict:
        rooms = self.room_repository.get_all(limit=limit, offset=offset, search=search)

        for room in rooms:
            for user in room.users:
                if user.id != g.user_id:
                    room.partner = user
                    break

        return self.response_ok([{
            'id': room.id,
            'user': {
                'id': room.partner.id,
                'name': room.partner.name,
                'first_name': room.partner.first_name,
                'last_name': room.partner.last_name,
                'image': self.get_dict_items(room.partner.image) if room.partner.image else None
            }
        } for room in rooms])
