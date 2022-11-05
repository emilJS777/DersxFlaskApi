from src.__Parents.Controller import Controller
from .PublicationLikeService import PublicationLikeService
from .PublicationLikeRepository import PublicationLikeRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class PublicationLikeController(Controller):
    publication_like_service: PublicationLikeService = PublicationLikeService(PublicationLikeRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.publication_like_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.publication_like_service.delete(self.arguments.get("publication_id"))
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.publication_like_service.get(publication_id=self.arguments.get('publication_id'))
        return res
