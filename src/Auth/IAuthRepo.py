from abc import ABC, abstractmethod
from src.__Parents.Service import Service


class IAuthRepo(ABC):
    @abstractmethod
    def generate_tokens(self, user_id: int):
        pass

    @abstractmethod
    def delete_by_user_id(self, user_id: int):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int):
        pass

