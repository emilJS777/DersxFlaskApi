from src.__Parents.Controller import Controller
from .ForumDiscussionService import ForumDiscussionService
from .ForumDiscussionRepository import ForumDiscussionRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .ForumDiscussionValidator import forum_discussion_schema


class ForumDiscussionController(Controller):
    forum_discussion_service: ForumDiscussionService = ForumDiscussionService(ForumDiscussionRepository())

    @expects_json(forum_discussion_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.forum_discussion_service.create(self.request.get_json())
        return res

    @expects_json(forum_discussion_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.forum_discussion_service.update(self.id, self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.forum_discussion_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.forum_discussion_service.get_by_id(self.id)
        else:
            res: dict = self.forum_discussion_service.get_all(forum_id=self.arguments.get("forum_id"))
        return res
