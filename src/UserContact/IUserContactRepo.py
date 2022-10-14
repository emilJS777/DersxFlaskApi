from abc import ABC, abstractmethod
from .UserContactModel import UserContact


class IUserContactRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, user_contact: UserContact, body: dict):
        pass

    @abstractmethod
    def delete(self, user_contact: UserContact):
        pass

    @abstractmethod
    def get_by_id(self, user_contact_id: int) -> UserContact:
        pass

    @abstractmethod
    def get_all(self, user_id) -> list[UserContact]:
        pass
