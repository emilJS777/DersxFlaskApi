from abc import ABC, abstractmethod
from .PublicationModel import Publication


class IPublicationRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> Publication:
        pass

    @abstractmethod
    def update(self, publication: Publication, body: dict):
        pass

    @abstractmethod
    def delete(self, publication: Publication):
        pass

    @abstractmethod
    def get_by_id(self, publication_id: int) -> Publication:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int, creator_id: int or None = None, liked_id: int or None = None) -> list[Publication]:
        pass
