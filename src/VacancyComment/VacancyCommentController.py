from src.__Parents.Controller import Controller
from .VacancyCommentService import VacancyCommentService
from .VacancyCommentRepository import VacancyCommentRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .VacancyCommentValidator import vacancy_comment_schema


class VacancyCommentController(Controller):
    vacancy_comment_service: VacancyCommentService = VacancyCommentService(VacancyCommentRepository())

    @expects_json(vacancy_comment_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.vacancy_comment_service.create(self.request.get_json())
        return res

    @expects_json(vacancy_comment_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.vacancy_comment_service.update(vacancy_comment_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.vacancy_comment_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.vacancy_comment_service.get_by_id(self.id)
        else:
            res: dict = self.vacancy_comment_service.get_all(
                page=self.page,
                per_page=self.per_page,
                vacancy_id=int(self.arguments.get('vacancy_id')))
        return res
