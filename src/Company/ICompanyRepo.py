from abc import ABC, abstractmethod
from .CompanyModel import Company


class ICompanyRepo(ABC):
    @abstractmethod
    def create(self, body: dict, rubrics: list) -> Company:
        pass

    @abstractmethod
    def update(self, company: Company, body: dict, rubrics: list):
        pass

    @abstractmethod
    def delete(self, company: Company):
        pass

    @abstractmethod
    def get_by_id(self, company_id: int) -> Company:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int, search: str or None, user_id: int or None, rubric_ids: list[int] or None):
        pass
