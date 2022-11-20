from abc import ABC, abstractmethod
from .MessageModel import Message


class IMessageRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, message: Message, body: dict):
        pass

    @abstractmethod
    def delete(self, message: Message):
        pass

    @abstractmethod
    def get_by_id(self, message_id: int) -> Message:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int, room_id: int) -> list[Message]:
        pass
