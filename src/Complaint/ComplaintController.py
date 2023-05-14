from src.Auth.AuthMiddleware import AuthMiddleware
from .ComplaintService import ComplaintService
from .ComplaintRepository import ComplaintRepository
from ..__Parents.Controller import Controller


class ComplaintController(Controller):
    complaint_service: ComplaintService = ComplaintService(ComplaintRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.complaint_service.create(body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.complaint_service.delete(complaint_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.complaint_service.get_all()
        return res
        