from abc import ABC, abstractmethod
from .ServiceModel import Service


class IServiceRepo(ABC):
    @abstractmethod
    def create(self, body: dict, categories: list) -> Service:
        pass

    @abstractmethod
    def update(self, service: Service, body: dict, categories: list):
        pass

    @abstractmethod
    def delete(self, service: Service):
        pass

    @abstractmethod
    def get_by_id(self, service_id: int) -> Service:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, rubric_id: int or None, category_ids: list or None, search: str or None, creator_id: int or None = None):
        pass
