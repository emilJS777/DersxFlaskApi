from .IRoomUserRepo import IRoomUserRepo
from .RoomUserModel import RoomUser
from flask import g


class RoomUserRepository(IRoomUserRepo):
    def get_by_id(self, room_id: int) -> RoomUser:
        return RoomUser.query.filter_by(room_id=room_id, user_id=g.user_id).first()

    def get_all(self) -> list[RoomUser]:
        return RoomUser.query.filter_by(user_id=g.user_id).all()

    def hidden(self, room_user: RoomUser):
        room_user.hidden = True
        room_user.update_db()

    def show(self, rooms_user: list[RoomUser]):
        for room_user in rooms_user:
            room_user.hidden = False
        RoomUser.update_db()

