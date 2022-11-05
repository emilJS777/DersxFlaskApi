from abc import ABC, abstractmethod
from .PublicationLikeModel import PublicationLike


class IPublicationLikeRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def delete(self, publication_like: PublicationLike):
        pass

    @abstractmethod
    def get(self, publication_like_id: int or None = None, publication_id: int or None = None, user_id: int or None = None) -> PublicationLike:
        pass
