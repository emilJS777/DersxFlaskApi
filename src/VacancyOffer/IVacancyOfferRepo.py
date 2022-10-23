from abc import ABC, abstractmethod
from .VacancyOfferModel import VacancyOffer


class IVacancyOfferRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, vacancy_offer: VacancyOffer, body: dict):
        pass

    @abstractmethod
    def delete(self, vacancy_offer: VacancyOffer):
        pass

    @abstractmethod
    def delete_all(self, vacancy_id: int):
        pass

    @abstractmethod
    def get_by_id(self, vacancy_offer_id: int) -> VacancyOffer:
        pass

    @abstractmethod
    def get_by_vacancy_id_creator_id(self, vacancy_id: int, creator_id: int) -> VacancyOffer:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, vacancy_id: int):
        pass
