from src.__Parents.Controller import Controller
from .PublicationImageService import PublicationImageService
from .PublicationImageRepository import PublicationImageRepository
from src.Publication.PublicationRepository import PublicationRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class PublicationImageController(Controller):
    publication_image_service: PublicationImageService = PublicationImageService(PublicationImageRepository(), PublicationRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.publication_image_service.create(publication_id=int(self.arguments.get('publication_id')), image=self.request.files['image'])
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.publication_image_service.delete(int(self.arguments.get('publication_id')))
        return res
