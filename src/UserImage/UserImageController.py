from src.__Parents.Controller import Controller
from .UserImageService import UserImageService
from .UserImageRepository import UserImageRepository
from src.User.UserRepository import UserRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class UserImageController(Controller):
    user_image_service: UserImageService = UserImageService(UserImageRepository(), UserRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.user_image_service.create(self.request.files["image"])
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.user_image_service.delete(self.arguments.get('filename'))
        return res

    def get(self) -> dict:
        res: dict = self.user_image_service.get_by_filename(self.arguments.get('filename'))
        return res
