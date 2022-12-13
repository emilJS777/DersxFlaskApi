from abc import ABC, abstractmethod
from .CompanyModel import Company


class ICompanyRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, company: Company, body: dict):
        pass

    @abstractmethod
    def delete(self, company: Company):
        pass

    @abstractmethod
    def get_by_id(self, company_id: int) -> Company:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str or None):
        pass
