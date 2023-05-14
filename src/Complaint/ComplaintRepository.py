from flask import g
from .IComplaintRepo import IComplaintRepo
from .ComplaintModel import Complaint


class ComplaintRepository(IComplaintRepo):
    def create(self, body: dict):
        complaint: Complaint = Complaint()
        complaint.user_id = g.user_id
        complaint.publication_id = body.get('publication_id')
        complaint.vacancy_id = body.get('vacancy_id')
        complaint.save_db()
        
    def delete(self, complaint: Complaint):
        complaint.delete_db()

    def get_by_id(self, complaint_id: int) -> Complaint:
        complaint: Complaint = Complaint.query.filter_by(id=complaint_id).first()
        return complaint

    def get_all(self) -> list[Complaint]:
        complaints: list[Complaint] = Complaint.query.filter_by().all()
        return complaints
        