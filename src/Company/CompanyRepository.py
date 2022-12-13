from .ICompanyRepo import ICompanyRepo
from .CompanyModel import Company
from flask import g


class CompanyRepository(ICompanyRepo):

    def create(self, body: dict):
        company: Company = Company()
        company.title = body['title']
        company.short_description = body['short_description']
        company.long_description = body['long_description']
        company.creator_id = g.user_id
        company.save_db()

    def update(self, company: Company, body: dict):
        company.title = body['title']
        company.short_description = body['short_description']
        company.long_description = body['long_description']
        company.update_db()

    def delete(self, company: Company):
        company.delete_db()

    def get_by_id(self, company_id: int) -> Company:
        company: Company = Company.query.filter_by(id=company_id).first()
        return company

    def get_all(self, page: int, per_page: int, search: str or None):
        companies = Company.query.filter(Company.title.like(f"%{search}%")).paginate(page=page, per_page=per_page)
        return companies
