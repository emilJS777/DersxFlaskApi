from src.__Parents.Service import Service
from .ICompanyRepo import ICompanyRepo
from ..__Parents.Repository import Repository
from flask import g


class CompanyService(Service, Repository):
    def __init__(self, company_repository: ICompanyRepo):
        self.company_repository: ICompanyRepo = company_repository

    def create(self, body: dict) -> dict:
        self.company_repository.create(body)
        return self.response_created('компания создана')

    def update(self, company_id: int, body: dict) -> dict:
        company = self.company_repository.get_by_id(company_id)
        if not company or not company.creator_id == g.user_id:
            return self.response_not_found('компания не найдена')
        self.company_repository.update(company=company, body=body)
        return self.response_updated('компания обновлена')

    def delete(self, company_id: int) -> dict:
        company = self.company_repository.get_by_id(company_id)
        if not company or not company.creator_id == g.user_id:
            return self.response_not_found('компания не найдена')
        self.company_repository.delete(company)
        return self.response_deleted('компания удалена')

    def get_by_id(self, company_id: int) -> dict:
        company = self.company_repository.get_by_id(company_id)
        return self.response_ok(self.get_dict_items(company))

    def get_all(self, page: int, per_page: int, search: str or None) -> dict:
        companies = self.company_repository.get_all(page=page, per_page=per_page, search=search)
        return self.response_ok(self.get_page_items(companies))
