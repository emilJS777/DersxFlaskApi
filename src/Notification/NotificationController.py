from src.__Parents.Controller import Controller
from .NotificationService import NotificationService
from .NotificationRepository import NotificationRepository
from ..Socketio.Socketio import Socketio
from src.Auth.AuthMiddleware import AuthMiddleware


class NotificationController(Controller):
    notification_service: NotificationService = NotificationService(NotificationRepository(), Socketio())

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.notification_service.get_by_id(notification_id=self.id)
        else:
            res: dict = self.notification_service.get_all()
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.notification_service.delete(self.id)
        return res
