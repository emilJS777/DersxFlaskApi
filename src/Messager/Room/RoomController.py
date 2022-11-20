from src.__Parents.Controller import Controller
from .RoomService import RoomService
from .RoomRepository import RoomRepository
from src.User.UserRepository import UserRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class RoomController(Controller):
    room_service: RoomService = RoomService(RoomRepository(), UserRepository())

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.room_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.arguments.get('user_id'):
            res: dict = self.room_service.get(self.arguments.get('user_id'))
        else:
            res: dict = self.room_service.get_all(limit=self.arguments.get('limit'),
                                                  offset=self.arguments.get('offset'))
        return res
