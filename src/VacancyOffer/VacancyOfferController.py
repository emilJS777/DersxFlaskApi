from src.__Parents.Controller import Controller
from .VacancyOfferService import VacancyOfferService
from .VacancyOfferRepository import VacancyOfferRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .VacancyOfferValidator import vacancy_offer_schema


class VacancyOfferController(Controller):
    vacancy_offer_service: VacancyOfferService = VacancyOfferService(VacancyOfferRepository())

    @expects_json(vacancy_offer_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.vacancy_offer_service.create(self.request.get_json())
        return res

    @expects_json(vacancy_offer_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.vacancy_offer_service.update(vacancy_offer_id=self.id, body=self.request.get_json())
        return res
    
    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.vacancy_offer_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.vacancy_offer_service.get_by_id(self.id)
        else:
            res: dict = self.vacancy_offer_service.get_all(
                page=self.page,
                per_page=self.per_page,
                vacancy_id=self.arguments.get('vacancy_id'))
        return res
