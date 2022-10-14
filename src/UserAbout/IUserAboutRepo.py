from abc import ABC, abstractmethod
from .UserAboutModel import UserAbout


class IUserAboutRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, user_about: UserAbout, body: dict):
        pass

    @abstractmethod
    def delete(self, user_about: UserAbout):
        pass

    @abstractmethod
    def get_by_id(self, user_about_id: int) -> UserAbout:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[UserAbout]:
        pass
