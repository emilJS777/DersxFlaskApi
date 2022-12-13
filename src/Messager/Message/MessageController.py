from src.__Parents.Controller import Controller
from .MessageRepository import MessageRepository
from .MessageService import MessageService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .MessageValidator import message_schema
from src.Socketio.Socketio import Socketio


class MessageController(Controller):
    message_service: MessageService = MessageService(MessageRepository(), Socketio())

    @AuthMiddleware.check_authorize
    @expects_json(message_schema)
    def post(self) -> dict:
        res: dict = self.message_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @expects_json(message_schema)
    def put(self) -> dict:
        res: dict = self.message_service.update(message_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def patch(self) -> dict:
        res: dict = self.message_service.read(self.id)
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.message_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.message_service.get_by_id(self.id)
        elif self.arguments.get('limit'):
            res: dict = self.message_service.get_all(
                limit=self.arguments.get('limit'),
                offset=self.arguments.get('offset'),
                room_id=int(self.arguments.get('room_id')))
        else:
            res: dict = self.message_service.get_not_read()
        return res
