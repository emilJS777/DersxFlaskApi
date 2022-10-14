from abc import ABC, abstractmethod
from .GenderModel import Gender


class IGenderRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, gender: Gender, body: dict):
        pass

    @abstractmethod
    def delete(self, gender: Gender):
        pass

    @abstractmethod
    def get_by_id(self, gender_id: int) -> Gender:
        pass

    @abstractmethod
    def get_all(self) -> list[Gender]:
        pass
