from src.__Parents.Controller import Controller
from .FriendService import FriendService
from .FriendRepository import FriendRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from ..User.UserRepository import UserRepository
from ..Socketio.Socketio import Socketio


class FriendController(Controller):
    friend_service: FriendService = FriendService(FriendRepository(), UserRepository(), Socketio())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.friend_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.friend_service.update(friend_id=self.id, user_id=self.arguments.get("user_id"))
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.friend_service.delete(friend_id=self.id, user_id=self.arguments.get('user_id'))
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.arguments.get('page') and self.arguments.get('user_id'):
            res: dict = self.friend_service.get_all(page=int(self.arguments.get('page')),
                                                    per_page=int(self.arguments.get('per_page')),
                                                    user_id=int(self.arguments.get('user_id')))

        elif self.arguments.get('page') and not self.arguments.get('user_id'):
            res: dict = self.friend_service.get_all_requests(
                page=int(self.arguments.get('page')),
                per_page=int(self.arguments.get('per_page')))

        else:
            res: dict = self.friend_service.get_by_user_id(self.arguments.get('user_id'))

        return res
