from .SkillService import SkillService
from .SkillRepository import SkillRepository
from ..Category.CategoryRepository import CategoryRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .SkillValidator import skill_schema


class SkillController(Controller):
    skill_service: SkillService = SkillService(SkillRepository(), CategoryRepository())

    @expects_json(skill_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.skill_service.create(self.request.get_json())
        return res

    @expects_json(skill_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.skill_service.update(skill_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.skill_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.skill_service.get_by_id(self.id)
        else:
            res: dict = self.skill_service.get_all(user_id=self.arguments.get('user_id'))
        return res
