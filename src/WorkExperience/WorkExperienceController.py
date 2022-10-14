from src.__Parents.Controller import Controller
from .WorkExperienceService import WorkExperienceService
from .WorkExperienceRepository import WorkExperienceRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .WorkExperienceValidator import work_experience_schema


class WorkExperienceController(Controller):
    work_experience_service: WorkExperienceService = WorkExperienceService(WorkExperienceRepository())

    @expects_json(work_experience_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.work_experience_service.create(self.request.get_json())
        return res

    @expects_json(work_experience_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.work_experience_service.update(work_experience_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.work_experience_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.work_experience_service.get_by_id(self.id)
        else:
            res: dict = self.work_experience_service.get_all(user_id=self.arguments.get('user_id'))
        return res