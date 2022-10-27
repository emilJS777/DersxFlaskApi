from abc import ABC, abstractmethod
from .ServiceImageModel import ServiceImage


class IServiceImageRepo(ABC):
    @abstractmethod
    def create(self, filename: str, service_id: int):
        pass

    @abstractmethod
    def update(self, service_image: ServiceImage, filename: str):
        pass

    @abstractmethod
    def delete(self, service_image: ServiceImage):
        pass

    @abstractmethod
    def get_by_id(self, service_image_id: int) -> ServiceImage:
        pass

    @abstractmethod
    def get_by_filename(self, filename: str) -> ServiceImage:
        pass
