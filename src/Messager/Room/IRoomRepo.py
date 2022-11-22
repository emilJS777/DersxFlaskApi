from abc import ABC, abstractmethod
from .RoomModel import Room


class IRoomRepo(ABC):
    @abstractmethod
    def create(self, users: list) -> Room:
        pass

    @abstractmethod
    def delete(self, room: Room):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Room:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int, search: str) -> list[Room]:
        pass
