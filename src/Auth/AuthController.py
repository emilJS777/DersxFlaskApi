from src.__Parents.Controller import Controller
from .AuthService import AuthService
from .AuthRepository import AuthRepository
from ..User.UserRepository import UserRepository
from flask_jwt_extended import jwt_required
from .AuthMiddleware import AuthMiddleware


class AuthController(Controller):
    auth_service = AuthService(auth_repository=AuthRepository(),
                               user_repository=UserRepository())

    def post(self):
        return self.auth_service.login(body=self.request.get_json())

    @jwt_required(refresh=True)
    def put(self):
        return self.auth_service.refresh()

    @AuthMiddleware.check_authorize
    def delete(self):
        return self.auth_service.logout()

    @AuthMiddleware.check_authorize
    def get(self):
        return self.auth_service.get_profile()
