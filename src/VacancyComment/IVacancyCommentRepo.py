from abc import ABC, abstractmethod
from .VacancyCommentModel import VacancyComment


class IVacancyCommentRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, vacancy_comment: VacancyComment, body: dict):
        pass

    @abstractmethod
    def delete(self, vacancy_comment: VacancyComment):
        pass

    @abstractmethod
    def delete_all(self, vacancy_id: int):
        pass

    @abstractmethod
    def get_by_id(self, vacancy_comment_id: int) -> VacancyComment:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, vacancy_id: int) -> list[VacancyComment]:
        pass
