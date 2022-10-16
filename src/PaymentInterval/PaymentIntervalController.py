from .PaymentIntervalService import PaymentIntervalService
from .PaymentIntervalRepository import PaymentIntervalRepository
from ..__Parents.Controller import Controller


class PaymentIntervalController(Controller):
    payment_interval_service: PaymentIntervalService = PaymentIntervalService(PaymentIntervalRepository())

    def post(self) -> dict:
        res: dict = self.payment_interval_service.create(self.request.get_json())
        return res

    def put(self) -> dict:
        res: dict = self.payment_interval_service.update(payment_interval_id=self.id, body=self.request.get_json())
        return res

    def delete(self) -> dict:
        res: dict = self.payment_interval_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.payment_interval_service.get_by_id(self.id)
        else:
            res: dict = self.payment_interval_service.get_all()
        return res
    