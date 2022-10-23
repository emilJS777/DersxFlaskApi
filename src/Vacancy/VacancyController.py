import ast
from src.__Parents.Controller import Controller
from .VacancyService import VacancyService
from .VacancyRepository import VacancyRepository
from src.Category.CategoryRepository import CategoryRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .VacancyValidator import vacancy_schema
from src.VacancyOffer.VacancyOfferRepository import VacancyOfferRepository
from src.VacancyComment.VacancyCommentRepository import VacancyCommentRepository


class VacancyController(Controller):
    vacancy_service: VacancyService = VacancyService(VacancyRepository(),
                                                     CategoryRepository(),
                                                     VacancyOfferRepository(),
                                                     VacancyCommentRepository())

    @expects_json(vacancy_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.vacancy_service.create(self.request.get_json())
        return res

    @expects_json(vacancy_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.vacancy_service.update(vacancy_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.vacancy_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.vacancy_service.get_by_id(self.id)
        else:
            res: dict = self.vacancy_service.get_all(
                page=self.page,
                per_page=self.per_page,
                search=self.arguments.get('search') or None,
                rubric_id=self.arguments.get('rubric_id') or None,
                category_ids=ast.literal_eval(self.arguments.get('category_ids')),
                payment_interval_ids=ast.literal_eval(self.arguments.get('payment_interval_ids')),
                creator_id=self.arguments.get('creator_id') or None,
                price_start=self.arguments.get('price_start') or None,
                price_end=self.arguments.get('price_end') or None)
        return res
