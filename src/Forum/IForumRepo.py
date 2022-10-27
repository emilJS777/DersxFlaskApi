from abc import ABC, abstractmethod
from .ForumModel import Forum


class IForumRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, forum: Forum, body: dict):
        pass

    @abstractmethod
    def delete(self, forum: Forum):
        pass

    @abstractmethod
    def get_by_id(self, forum_id: int) -> Forum:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, rubric_id: int or None, search: str or None, creator_id: int or None):
        pass
