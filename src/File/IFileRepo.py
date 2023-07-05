from .FileModel import File
from abc import ABC, abstractmethod

class IFileRepo(ABC):
    @abstractmethod
    def create(self, file, offer_id: int = None):
        pass

    @abstractmethod
    def delete(self, file: File):
        pass

    @abstractmethod
    def get(self, filename: str) -> File:
        pass
