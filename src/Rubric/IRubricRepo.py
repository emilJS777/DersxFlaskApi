from abc import ABC, abstractmethod
from .RubricModel import Rubric


class IRubricRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, rubric: Rubric, body: dict):
        pass

    @abstractmethod
    def delete(self, rubric: Rubric):
        pass

    @abstractmethod
    def get_by_id(self, rubric_id: int) -> Rubric:
        pass

    @abstractmethod
    def get_all(self) -> list[Rubric]:
        pass
