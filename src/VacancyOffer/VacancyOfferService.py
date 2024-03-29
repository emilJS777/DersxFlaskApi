from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IVacancyOfferRepo import IVacancyOfferRepo
from flask import g
from ..File.IFileRepo import IFileRepo
from ..Notification.INotificationRepo import INotificationRepo
from ..Socketio.ISocketio import ISocketio


class VacancyOfferService(Service, Repository):
    def __init__(self, vacancy_offer_repository: IVacancyOfferRepo, notification_repository: INotificationRepo, file_repository: IFileRepo):
        self.vacancy_offer_repository: IVacancyOfferRepo = vacancy_offer_repository
        self.notification_repository: INotificationRepo = notification_repository
        self.file_repository: IFileRepo = file_repository

    def create(self, body: dict) -> dict:
        if self.vacancy_offer_repository.get_by_vacancy_id_creator_id(vacancy_id=body['vacancy_id'], creator_id=g.user_id):
            return self.response_conflict(msg_rus='в данной вакансии у вас уже есть предложение',
                                          msg_eng='you already have an offer for this job',
                                          msg_arm='դուք արդեն ունեք առաջարկ այս աշխատանքի համար')
        vacancy_offer = self.vacancy_offer_repository.create(body)
        # NOTIFICATION
        self.notification_repository.create(user_id=vacancy_offer.vacancy.creator_id, vacancy_offer_id=vacancy_offer.id)
        return self.response_ok({"id": vacancy_offer.id})

    def update(self, vacancy_offer_id: int, body: dict) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer or not vacancy_offer.creator_id == g.user_id:
            return self.response_not_found(msg_rus='предложение не найдено',
                                           msg_eng='offer not found',
                                           msg_arm='առաջարկը չի գտնվել')
        self.vacancy_offer_repository.update(vacancy_offer=vacancy_offer, body=body)
        return self.response_updated(msg_rus='предложение успешно обновлено',
                                     msg_arm='առաջարկը հաջողությամբ թարմացվել է',
                                     msg_eng='offer successfully updated')

    def delete(self, vacancy_offer_id: int) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer or not vacancy_offer.vacancy.creator_id == g.user_id:
            return self.response_not_found(msg_rus='предложение не найдено',
                                           msg_eng='offer not found',
                                           msg_arm='առաջարկը չի գտնվել')
        self.vacancy_offer_repository.delete(vacancy_offer)
        self.file_repository.delete(file=vacancy_offer.file)
        return self.response_deleted(msg_rus='предложение успешно удалено',
                                     msg_arm='առաջարկը հաջողությամբ ջնջվեց',
                                     msg_eng='offer successfully deleted')

    def get_by_id(self, vacancy_offer_id: int) -> dict:
        vacancy_offer = self.vacancy_offer_repository.get_by_id(vacancy_offer_id)
        if not vacancy_offer:
            return self.response_not_found(msg_rus='предложение не найдено',
                                           msg_eng='offer not found',
                                           msg_arm='առաջարկը չի գտնվել')
        return self.response_ok({
            'id': vacancy_offer.id,
            'description': vacancy_offer.description,
            'payment_interval': self.get_dict_items(vacancy_offer.payment_interval),
            'price': vacancy_offer.price,
            'vacancy_id': vacancy_offer.vacancy_id,
            'file': {
                'id': vacancy_offer.file.id,
                'filename': vacancy_offer.file.filename,
            } if vacancy_offer.file else None
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
                                     'file': {
                                         'id': vacancy_offer.file.id,
                                         'filename': vacancy_offer.file.filename,
                                     } if vacancy_offer.file else None,
                                     'creator': {
                                        'id': vacancy_offer.creator.id,
                                        'name': vacancy_offer.creator.name,
                                        'first_name': vacancy_offer.creator.first_name,
                                        'last_name': vacancy_offer.creator.last_name,
                                        'image': self.get_dict_items(vacancy_offer.creator.image) if vacancy_offer.creator.image else None
                                    },
                                 } for vacancy_offer in vacancy_offers.items]})
