from ..__Parents.Repository import Repository
from .IComplaintRepo import IComplaintRepo
from ..__Parents.Service import Service
from flask import g


class ComplaintService(Service, Repository):
    def __init__(self, complaint_repository: IComplaintRepo):
        self.complaint_repository: IComplaintRepo = complaint_repository

    def create(self, body: dict) -> dict:
        self.complaint_repository.create(body=body)
        return self.response_created()

    def delete(self, complaint_id: int) -> dict:
        complaint = self.complaint_repository.get_by_id(complaint_id)
        if not complaint or complaint.user_id != g.user_id:
            return self.response_not_found()
        self.complaint_repository.delete(complaint)
        return self.response_deleted()

    def get_all(self) -> dict:
        complaints: list = self.complaint_repository.get_all()
        return self.response_ok(self.get_array_items(complaints))
        