from abc import ABC, abstractmethod
from .PaymentIntervalModel import PaymentInterval


class IPaymentIntervalRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, payment_interval: PaymentInterval, body: dict):
        pass

    @abstractmethod
    def delete(self, payment_interval: PaymentInterval):
        pass

    @abstractmethod
    def get_by_id(self, payment_interval_id: int) -> PaymentInterval:
        pass

    @abstractmethod
    def get_all(self) -> list[PaymentInterval]:
        pass
