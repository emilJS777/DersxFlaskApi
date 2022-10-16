from abc import ABC, abstractmethod
from .VacancyModel import Vacancy


class IVacancyRepo(ABC):
    @abstractmethod
    def create(self, body: dict, categories: list):
        pass

    @abstractmethod
    def update(self, vacancy: Vacancy, body: dict, categories: list):
        pass

    @abstractmethod
    def delete(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_by_id(self, vacancy_id: int) -> Vacancy:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str or None, rubric_id: int or None, creator_id: int or None,
                payment_interval_ids: list[int], category_ids: list, price_start: float, price_end: float):
        pass
