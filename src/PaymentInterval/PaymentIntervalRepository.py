from .IPaymentIntervalRepo import IPaymentIntervalRepo
from .PaymentIntervalModel import PaymentInterval


class PaymentIntervalRepository(IPaymentIntervalRepo):

    def create(self, body: dict):
        payment_interval: PaymentInterval = PaymentInterval()
        payment_interval.title = body['title']
        payment_interval.description = body['description']
        payment_interval.save_db()

    def update(self, payment_interval: PaymentInterval, body: dict):
        payment_interval.title = body['title']
        payment_interval.description = body['description']
        payment_interval.update_db()

    def delete(self, payment_interval: PaymentInterval):
        payment_interval.delete_db()

    def get_by_id(self, payment_interval_id: int) -> PaymentInterval:
        payment_interval: PaymentInterval = PaymentInterval.query.filter_by(id=payment_interval_id).first()
        return payment_interval

    def get_all(self) -> list[PaymentInterval]:
        payment_intervals: list[PaymentInterval] = PaymentInterval.query.all()
        return payment_intervals
