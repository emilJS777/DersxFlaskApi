from .IVacancyOfferRepo import IVacancyOfferRepo
from .VacancyOfferModel import VacancyOffer
from flask import g


class VacancyOfferRepository(IVacancyOfferRepo):
    def create(self, body: dict):
        vacancy_offer: VacancyOffer = VacancyOffer()
        vacancy_offer.vacancy_id = body['vacancy_id']
        vacancy_offer.price = body['price']
        vacancy_offer.description = body['description']
        vacancy_offer.payment_interval_id = body['payment_interval_id']
        vacancy_offer.creator_id = g.user_id
        vacancy_offer.save_db()

    def update(self, vacancy_offer: VacancyOffer, body: dict):
        vacancy_offer.price = body['price']
        vacancy_offer.description = body['description']
        vacancy_offer.payment_interval_id = body['payment_interval_id']
        vacancy_offer.update_db()

    def delete(self, vacancy_offer: VacancyOffer):
        vacancy_offer.delete_db()

    def delete_all(self, vacancy_id: int):
        VacancyOffer.query.filter_by(vacancy_id=vacancy_id).delete()

    def get_by_id(self, vacancy_offer_id: int) -> VacancyOffer:
        vacancy_offer: VacancyOffer = VacancyOffer.query.filter_by(id=vacancy_offer_id).first()
        return vacancy_offer

    def get_by_vacancy_id_creator_id(self, vacancy_id: int, creator_id: int) -> VacancyOffer:
        vacancy_offer: VacancyOffer = VacancyOffer.query.filter_by(vacancy_id=vacancy_id, creator_id=creator_id).first()
        return vacancy_offer

    def get_all(self, page: int, per_page: int, vacancy_id: int):
        vacancy_offers = VacancyOffer.query.filter_by(vacancy_id=vacancy_id)\
            .order_by(-VacancyOffer.creation_date).paginate(page=page, per_page=per_page)
        return vacancy_offers
