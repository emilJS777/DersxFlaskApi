from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IPaymentIntervalRepo import IPaymentIntervalRepo


class PaymentIntervalService(Service, Repository):

    def __init__(self, payment_interval_repository: IPaymentIntervalRepo):
        self.payment_interval_repository: IPaymentIntervalRepo = payment_interval_repository

    def create(self, body: dict) -> dict:
        self.payment_interval_repository.create(body)
        return self.response_created('интервал оплаты создан')

    def update(self, payment_interval_id: int, body: dict) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found('интервал оплаты не найден')
        self.payment_interval_repository.update(
            payment_interval=payment_interval,
            body=body)
        return self.response_updated('интервал оплаты обновлен')

    def delete(self, payment_interval_id: int) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found('интервал оплаты не найден')
        self.payment_interval_repository.delete(payment_interval)
        return self.response_deleted('интервал оплаты удален')

    def get_by_id(self, payment_interval_id: int) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found('интервал оплаты не найден')
        return self.response_ok(self.get_dict_items(payment_interval))

    def get_all(self) -> dict:
        payment_intervals = self.payment_interval_repository.get_all()
        return self.response_ok(self.get_array_items(payment_intervals))
