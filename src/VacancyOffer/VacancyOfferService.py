from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IVacancyOfferRepo import IVacancyOfferRepo
from flask import g


class VacancyOfferService(Service, Repository):

    def __init__(self, vacancy_offer_repository: IVacancyOfferRepo):
        self.vacancy_offer_repository: IVacancyOfferRepo = vacancy_offer_repository

    def create(self, body: dict) -> dict:
        if self.vacancy_offer_repository.get_by_vacancy_id_creator_id(vacancy_id=body['vacancy_id'], creator_id=g.user_id):
            return self.response_conflict('в данной вакансии у вас уже есть предложение')

        self.vacancy_offer_repository.create(body)
        return self.response_created('предложение успешно создано')

    def update(self, vacancy_offer_id: int, body: dict) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer or not vacancy_offer.creator_id == g.user_id:
            return self.response_not_found('предложение не найдено')
        self.vacancy_offer_repository.update(vacancy_offer=vacancy_offer, body=body)
        return self.response_updated('предложение успешно обновлено')

    def delete(self, vacancy_offer_id: int) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer or not vacancy_offer.creator_id == g.user_id:
            return self.response_not_found('предложение не найдено')
        self.vacancy_offer_repository.delete(vacancy_offer)
        return self.response_deleted('предложение успешно удалено')

    def get_by_id(self, vacancy_offer_id: int) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer:
            return self.response_not_found('предложение не найдено')
        return self.response_ok({
            'id': vacancy_offer.id,
            'description': vacancy_offer.description,
            'payment_interval': self.get_dict_items(vacancy_offer.payment_interval),
            'price': vacancy_offer.price,
            'vacancy_id': vacancy_offer.vacancy_id
        })

    def get_all(self, page: int, per_page: int, vacancy_id: int) -> dict:
        vacancy_offers = self.vacancy_offer_repository.get_all(page=page, per_page=per_page, vacancy_id=vacancy_id)
        return self.response_ok({'total': vacancy_offers.total,
                                 'page': vacancy_offers.page,
                                 'pages': vacancy_offers.pages,
                                 'per_page': vacancy_offers.per_page,
                                 'items': [{
                                     'id': vacancy_offer.id,
                                     'description': vacancy_offer.description,
                                     'price': vacancy_offer.price,
                                     'payment_interval': self.get_dict_items(vacancy_offer.payment_interval),
                                     'creator_id': vacancy_offer.creator_id,
                                     'creation_date': vacancy_offer.creation_date,
                                     'creator': {
                                        'id': vacancy_offer.creator.id,
                                        'name': vacancy_offer.creator.name,
                                        'first_name': vacancy_offer.creator.first_name,
                                        'last_name': vacancy_offer.creator.last_name,
                                        'image': self.get_encode_image(vacancy_offer.creator.image.filename) if vacancy_offer.creator.image.filename else None
                                    },
                                 } for vacancy_offer in vacancy_offers.items]})
