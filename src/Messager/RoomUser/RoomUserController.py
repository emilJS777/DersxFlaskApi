from .RoomUserService import RoomUserService
from .RoomUserRepository import RoomUserRepository
from ...__Parents.Controller import Controller


class RoomUserController(Controller):
    room_user_service: RoomUserService = RoomUserService(RoomUserRepository())

    def put(self) -> dict:
        if self.arguments.get('room_id'):
            res: dict = self.room_user_service.hidden(room_id=self.arguments.get('room_id'))
        else:
            res: dict = self.room_user_service.show_all()
        return res
