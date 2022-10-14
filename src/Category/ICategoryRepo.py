from abc import ABC, abstractmethod
from .CategoryModel import Category


class ICategoryRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, category: Category, body: dict):
        pass

    @abstractmethod
    def delete(self, category: Category):
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def get_all(self, rubric_id: int or None = None, ids: list[int] or None = None) -> list[Category]:
        pass
