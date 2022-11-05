from src.__Parents.Controller import Controller
from .PublicationRepository import PublicationRepository
from .PublicationService import PublicationService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .PublicationValidator import publication_schema
from src.PublicationImage.PublicationImageRepository import PublicationImageRepository


class PublicationController(Controller):
    publication_service: PublicationService = PublicationService(PublicationRepository(), PublicationImageRepository())

    @expects_json(publication_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.publication_service.create(self.request.get_json())
        return res

    @expects_json(publication_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.publication_service.update(self.id, self.request.get_data())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.publication_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.publication_service.get_by_id(self.id)
        else:
            res: dict = self.publication_service.get_all(
                limit=self.arguments.get('limit'),
                offset=self.arguments.get('offset'),
                creator_id=self.arguments.get('creator_id'),
                liked_id=self.arguments.get('liked_id'))
        return res