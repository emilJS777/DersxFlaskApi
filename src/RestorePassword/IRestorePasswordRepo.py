
from abc import ABC, abstractmethod
from .RestorePasswordModel import RestorePassword
from ..User.UserModel import User


class IRestorePasswordRepo(ABC):
    @abstractmethod
    def create(self, user_id: int, security_code: str):
        pass

    @abstractmethod
    def update(self, restore_password: RestorePassword, security_code: str):
        pass

    @abstractmethod
    def delete(self, restore_password: RestorePassword):
        pass

    @abstractmethod
    def restore_password(self, user: User, new_password: str):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int):
        pass

    @abstractmethod
    def get_by_security_code(self, security_code: str) -> RestorePassword:
        pass

    @abstractmethod
    def get_all(self) -> list[RestorePassword]:
        pass
        