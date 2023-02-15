from .ICompanyRepo import ICompanyRepo
from .CompanyModel import Company
from flask import g
from src.User.UserModel import User
from src.Rubric.RubricModel import Rubric


class CompanyRepository(ICompanyRepo):

    def create(self, body: dict, rubrics: list) -> Company:
        company: Company = Company()
        company.title = body['title']
        company.short_description = body['short_description']
        company.long_description = body['long_description']
        company.creator_id = g.user_id
        company.users = [g.user]
        company.rubrics = rubrics
        company.save_db()
        return company

    def update(self, company: Company, body: dict, rubrics: list):
        company.title = body['title']
        company.short_description = body['short_description']
        company.long_description = body['long_description']
        company.rubrics = rubrics
        company.update_db()

    def delete(self, company: Company):
        company.users = []
        company.delete_db()

    def get_by_id(self, company_id: int) -> Company:
        company: Company = Company.query.filter_by(id=company_id).first()
        return company

    def get_all(self, limit: int, offset: int, search: str or None, user_id: int or None, rubric_ids: list[int] or None):
        companies = Company.query\
            .filter(Company.title.like(f"%{search}%"))\
            .where(Company.users.any(User.id.in_([user_id])) if user_id else Company.id.isnot(None))\
            .where(Company.rubrics.any(Rubric.id.in_(rubric_ids)) if rubric_ids else Company.id.isnot(None))\
            .limit(limit).offset(offset).all()
        return companies
