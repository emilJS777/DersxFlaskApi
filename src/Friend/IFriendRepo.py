from abc import ABC, abstractmethod
from .FriendModel import Friend


class IFriendRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> Friend:
        pass

    @abstractmethod
    def update(self, friend: Friend) -> Friend:
        pass

    @abstractmethod
    def delete(self, friend: Friend):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Friend:
        pass

    @abstractmethod
    def get_by_id(self, friend_id: int) -> Friend:
        pass

    # @abstractmethod
    # def get_all_requests(self, page: int, per_page: int):
    #     pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, user_id: int):
        pass
