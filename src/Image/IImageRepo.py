from .ImageModel import Image
from abc import ABC, abstractmethod


class IImageRepo(ABC):
    @abstractmethod
    def create(self, image, user_id: int = None, service_id: int = None, publication_id: int = None, company_id: int = None, team_id: int = None):
        pass

    @abstractmethod
    def delete(self, image: Image):
        pass

    @abstractmethod
    def get(self, filename: str) -> Image:
        pass
