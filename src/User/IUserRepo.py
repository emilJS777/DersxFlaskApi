from abc import ABC, abstractmethod
from .UserModel import User


class IUserRepo(ABC):

    @abstractmethod
    def create(self, body: dict, admin: bool = False):
        pass

    @abstractmethod
    def update(self, user_id: int, body: dict):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, user_id: int, name: str):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, rubric_id: int or None, role_id: int or None, category_ids: list[int] or None,
                search: str or None, group_id: int or None, not_group_id: int or None):
        pass

    @abstractmethod
    def get_all_by_ids(self, user_ids: list[int]) -> list[User]:
        pass

    @abstractmethod
    def get_count(self) -> int:
        pass









