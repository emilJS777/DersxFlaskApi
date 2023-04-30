from abc import ABC, abstractmethod
from .EmailModel import Email


class IEmailRepo(ABC):
    @abstractmethod
    def create(self, user_id: int, body: dict):
        pass

    @abstractmethod
    def update(self, email: Email, body: dict):
        pass

    @abstractmethod
    def get_by_address(self, address: str):
        pass

    @abstractmethod
    def get_by_address_exclude_user_id(self, user_id: int, address: str):
        pass

    @abstractmethod
    def create_activation(self):
        pass

    @abstractmethod
    def update_activation_code(self, code):
        pass




