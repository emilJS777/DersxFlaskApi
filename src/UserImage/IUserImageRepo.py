from abc import ABC, abstractmethod
from .UserImageModel import UserImage


class IUserImageRepo(ABC):
    @abstractmethod
    def create(self, filename: str):
        pass

    @abstractmethod
    def delete(self, user_image: UserImage):
        pass

    @abstractmethod
    def get_by_id(self, user_image_id: int) -> UserImage:
        pass

    @abstractmethod
    def get_by_filename(self, filename: str) -> UserImage:
        pass
