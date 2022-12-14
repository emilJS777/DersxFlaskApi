from abc import ABC, abstractmethod
from .RoomUserModel import RoomUser


class IRoomUserRepo(ABC):
    @abstractmethod
    def get_by_id(self, room_id: int) -> RoomUser:
        pass

    @abstractmethod
    def get_all(self) -> list[RoomUser]:
        pass

    @abstractmethod
    def hidden(self, room_user: RoomUser):
        pass

    @abstractmethod
    def show(self, rooms_user: list[RoomUser]):
        pass
