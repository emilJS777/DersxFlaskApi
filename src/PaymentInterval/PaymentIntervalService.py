from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IPaymentIntervalRepo import IPaymentIntervalRepo


class PaymentIntervalService(Service, Repository):

    def __init__(self, payment_interval_repository: IPaymentIntervalRepo):
        self.payment_interval_repository: IPaymentIntervalRepo = payment_interval_repository

    def create(self, body: dict) -> dict:
        self.payment_interval_repository.create(body)
        return self.response_created(msg_rus='интервал оплаты создан',
                                     msg_eng='payment interval created',
                                     msg_arm='ստեղծվել է վճարման ընդմիջում')

    def update(self, payment_interval_id: int, body: dict) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found(msg_rus='интервал оплаты не найден',
                                           msg_arm='վճարման ընդմիջումն չի գտնվել',
                                           msg_eng='payment interval not found')
        self.payment_interval_repository.update(
            payment_interval=payment_interval,
            body=body)
        return self.response_updated(msg_rus='интервал оплаты обновлен',
                                     msg_eng='payment interval updated',
                                     msg_arm='վճարման ընդմիջումն թարմացվել է')

    def delete(self, payment_interval_id: int) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found(msg_rus='интервал оплаты не найден',
                                           msg_arm='վճարման ընդմիջումն չի գտնվել',
                                           msg_eng='payment interval not found')
        self.payment_interval_repository.delete(payment_interval)
        return self.response_not_found(msg_rus='интервал оплаты удален',
                                       msg_arm='վճարման ընդմիջումն ջնջված է',
                                       msg_eng='payment deleted')

    def get_by_id(self, payment_interval_id: int) -> dict:
        payment_interval = self.payment_interval_repository.get_by_id(payment_interval_id)
        if not payment_interval:
            return self.response_not_found(msg_rus='интервал оплаты не найден',
                                           msg_arm='վճարման ընդմիջումն չի գտնվել',
                                           msg_eng='payment interval not found')
        return self.response_ok(self.get_dict_items(payment_interval))

    def get_all(self) -> dict:
        payment_intervals = self.payment_interval_repository.get_all()
        return self.response_ok(self.get_array_items(payment_intervals))
