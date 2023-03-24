from .GroupService import GroupService
from .GroupRepository import GroupRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .GroupValidator import group_schema


class GroupController(Controller):
    group_service: GroupService = GroupService(GroupRepository())

    @expects_json(group_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.group_service.create(body=self.request.get_json())
        return res

    @expects_json(group_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.group_service.update(group_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.group_service.delete(group_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.group_service.get_by_id(self.id)
        else:
            res: dict = self.group_service.get_all(page=self.page, per_page=self.per_page, search=self.arguments.get('search'))
        return res
        