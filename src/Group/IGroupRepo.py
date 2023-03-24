from abc import ABC, abstractmethod
from .GroupModel import Group


class IGroupRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> Group:
        pass

    @abstractmethod
    def update(self, group: Group, body: dict):
        pass

    @abstractmethod
    def delete(self, group: Group):
        pass

    @abstractmethod
    def get_by_id(self, group_id: int) -> Group:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str):
        pass
        