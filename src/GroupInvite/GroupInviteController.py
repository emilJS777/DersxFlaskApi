from .GroupInviteService import GroupInviteService
from .GroupInviteRepository import GroupInviteRepository
from ..__Parents.Controller import Controller
from ..Notification.NotificationRepository import NotificationRepository
from ..Socketio.Socketio import Socketio
from ..Auth.AuthMiddleware import AuthMiddleware
from .GroupInviteService import GroupInviteService


class GroupInviteController(Controller):
    group_invite_service: GroupInviteService = GroupInviteService(GroupInviteRepository(), NotificationRepository(Socketio()))

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.group_invite_service.create(body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.group_invite_service.update(self.id)
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.group_invite_service.delete(group_id=self.arguments.get('group_id'), user_id=self.arguments.get('user_id'))
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.group_invite_service.get(group_id=self.arguments.get('group_id'), user_id=self.arguments.get('user_id'))
        return res
