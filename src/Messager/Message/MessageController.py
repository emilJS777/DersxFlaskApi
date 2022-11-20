from src.__Parents.Controller import Controller
from .MessageRepository import MessageRepository
from .MessageService import MessageService
from src.Auth.AuthMiddleware import AuthMiddleware


class MessageController(Controller):
    message_service: MessageService = MessageService(MessageRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.message_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.message_service.update(message_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.message_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.message_service.get_by_id(self.id)
        else:
            res: dict = self.message_service.get_all(
                limit=self.arguments.get('limit'),
                offset=self.arguments.get('offset'),
                room_id=int(self.arguments.get('room_id')))
        return res
