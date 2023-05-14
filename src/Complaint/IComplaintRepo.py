
from abc import ABC, abstractmethod
from .ComplaintModel import Complaint


class IComplaintRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def delete(self, complaint: Complaint):
        pass

    @abstractmethod
    def get_by_id(self, complaint_id: int) -> Complaint:
        pass

    @abstractmethod
    def get_all(self) -> list[Complaint]:
        pass
        