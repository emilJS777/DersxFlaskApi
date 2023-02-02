from src.__Parents.Controller import Controller
from .ImageService import ImageService
from .ImageRepository import ImageRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class ImageController(Controller):
    image_service: ImageService = ImageService(ImageRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.image_service.create(
            image=self.request.files['image'],
            user_id=self.arguments.get("user_id"),
            service_id=self.arguments.get('service_id'),
            publication_id=self.arguments.get('publication_id'),
            company_id=self.arguments.get('company_id'))
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.image_service.delete(self.arguments.get("filename"))
        return res

    def get(self):
        res = self.image_service.get(self.arguments.get("filename"))
        return res
