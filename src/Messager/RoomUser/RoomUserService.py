from src.__Parents.Service import Service
from .IRoomUserRepo import IRoomUserRepo


class RoomUserService(Service):

    def __init__(self, room_user_repository: IRoomUserRepo):
        self.room_user_repository: IRoomUserRepo = room_user_repository

    def hidden(self, room_id) -> dict:
        room_user = self.room_user_repository.get_by_id(room_id=room_id)
        self.room_user_repository.hidden(room_user=room_user)
        return self.response_updated()

    def show_all(self) -> dict:
        rooms_user = self.room_user_repository.get_all()
        self.room_user_repository.show(rooms_user)
        return self.response_updated()
