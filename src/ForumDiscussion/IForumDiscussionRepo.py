from abc import ABC, abstractmethod
from .ForumDiscussionModel import ForumDiscussion


class IForumDiscussionRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, forum_discussion: ForumDiscussion, body: dict):
        pass

    @abstractmethod
    def delete(self, forum_discussion: ForumDiscussion):
        pass

    @abstractmethod
    def delete_all(self, forum_id: int):
        pass

    @abstractmethod
    def get_by_id(self, forum_discussion_id: int) -> ForumDiscussion:
        pass

    @abstractmethod
    def get_all(self, forum_id: int) -> list[ForumDiscussion]:
        pass
