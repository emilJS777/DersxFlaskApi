from .UserAboutService import UserAboutService
from .UserAboutRepository import UserAboutRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .UserAboutValidator import user_about_schema


class UserAboutController(Controller):
    user_about_service: UserAboutService = UserAboutService(UserAboutRepository())

    @expects_json(user_about_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.user_about_service.create(self.request.get_json())
        return res

    @expects_json(user_about_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.user_about_service.update(user_about_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.user_about_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.user_about_service.get_by_id(self.id)
        else:
            res: dict = self.user_about_service.get_all(self.arguments.get('user_id'))
        return res
