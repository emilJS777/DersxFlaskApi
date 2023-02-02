from .PublicationCommentService import PublicationCommentService
from .PublicationCommentRepository import PublicationCommentRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .PublicationCommentValidator import publication_comment_schema


class PublicationCommentController(Controller):
    publication_comment_service: PublicationCommentService = PublicationCommentService(PublicationCommentRepository())

    @expects_json(publication_comment_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.publication_comment_service.create(self.request.get_json())
        return res

    @expects_json(publication_comment_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.publication_comment_service.update(
            publication_comment_id=self.id,
            body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.publication_comment_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.publication_comment_service.get_by_id(self.id)
        else:
            res: dict = self.publication_comment_service.get_all(
                limit=self.arguments.get('limit'),
                offset=self.arguments.get('offset'),
                publication_id=self.arguments.get('publication_id'))
        return res
