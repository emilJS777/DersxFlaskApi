from abc import ABC, abstractmethod


class ISocketio(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send(self, emit_name: str, data: dict, user_id: int):
        pass

    @abstractmethod
    def get_online(data: dict):
        pass
