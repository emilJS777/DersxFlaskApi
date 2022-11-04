from abc import ABC, abstractmethod
from .PublicationCommentModel import PublicationComment


class IPublicationCommentRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, publication_comment: PublicationComment, body: dict):
        pass

    @abstractmethod
    def delete(self, publication_comment: PublicationComment):
        pass

    @abstractmethod
    def get_by_id(self, publication_comment_id: int) -> PublicationComment:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int, publication_id: int) -> list[PublicationComment]:
        pass
