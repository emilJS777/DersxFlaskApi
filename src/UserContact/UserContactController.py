from .UserContactService import UserContactService
from .UserContactRepository import UserContactRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .UserContactValidator import user_contact_schema


class UserContactController(Controller):
    user_contact_service: UserContactService = UserContactService(UserContactRepository())

    @expects_json(user_contact_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.user_contact_service.create(self.request.get_json())
        return res

    @expects_json(user_contact_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.user_contact_service.update(user_contact_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.user_contact_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.user_contact_service.get_by_id(self.id)
        else:
            res: dict = self.user_contact_service.get_all(self.arguments.get('user_id'))
        return res
