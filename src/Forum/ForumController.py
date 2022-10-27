from .ForumService import ForumService
from .ForumRepository import ForumRepository
from src.ForumDiscussion.ForumDiscussionRepository import ForumDiscussionRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .ForumValidator import forum_schema


class ForumController(Controller):
    forum_service: ForumService = ForumService(ForumRepository(), ForumDiscussionRepository())

    @expects_json(forum_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.forum_service.create(self.request.get_json())
        return res

    @expects_json(forum_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.forum_service.update(forum_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.forum_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.forum_service.get_by_id(self.id)
        else:
            res: dict = self.forum_service.get_all(
                page=self.page,
                per_page=self.per_page,
                rubric_id=self.arguments.get('rubric_id'),
                search=self.arguments.get('search'),
                creator_id=self.arguments.get("creator_id"))
        return res
