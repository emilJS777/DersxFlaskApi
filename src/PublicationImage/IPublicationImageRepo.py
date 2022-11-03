from abc import ABC, abstractmethod
from .PublicationImageModel import PublicationImage


class IPublicationImageRepo(ABC):
    @abstractmethod
    def create(self, filename: str, publication_id: int):
        pass

    @abstractmethod
    def update(self, publication_image: PublicationImage, filename: str):
        pass

    @abstractmethod
    def delete(self, publication_image: PublicationImage):
        pass

    @abstractmethod
    def get_by_id(self, publication_image_id: int) -> PublicationImage:
        pass

    @abstractmethod
    def get_by_filename(self, filename: str) -> PublicationImage:
        pass
