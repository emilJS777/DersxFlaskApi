from src.__Parents.Service import Service
from .ICompanyRepo import ICompanyRepo
from ..Rubric.IRubricRepo import IRubricRepo
from ..__Parents.Repository import Repository
from flask import g


class CompanyService(Service, Repository):
    def __init__(self, company_repository: ICompanyRepo, rubric_repository: IRubricRepo):
        self.company_repository: ICompanyRepo = company_repository
        self.rubric_repository: IRubricRepo = rubric_repository

    def create(self, body: dict) -> dict:
        rubrics = self.rubric_repository.get_all(rubric_ids=body['rubric_ids'])
        company = self.company_repository.create(body=body, rubrics=rubrics)
        return self.response_ok({'id': company.id, 'msg': 'компания создано'})

    def update(self, company_id: int, body: dict) -> dict:
        company = self.company_repository.get_by_id(company_id)
        if not company or not company.creator_id == g.user_id:
            return self.response_not_found('компания не найдена')
        rubrics = self.rubric_repository.get_all(rubric_ids=body['rubric_ids'])
        self.company_repository.update(company=company, body=body, rubrics=rubrics)
        return self.response_updated('компания обновлена')

    def delete(self, company_id: int) -> dict:
        company = self.company_repository.get_by_id(company_id)
        if not company or not company.creator_id == g.user_id:
            return self.response_not_found('компания не найдена')
        self.company_repository.delete(company)
        return self.response_deleted('компания удалена')

    def get_by_id(self, company_id: int) -> dict:
        company = self.company_repository.get_by_id(company_id)
        return self.response_ok({
                'id': company.id,
                'title': company.title,
                'short_description': company.short_description,
                'long_description': company.long_description,
                'rubrics': self.get_array_items(company.rubrics),
                'creator_id': company.creator_id,
                'user_count': len(company.users),
                'my_company': True if g.user in company.users else None,
                'image': self.get_dict_items(company.image) if company.image else None
            })

    def get_all(self, limit: int, offset: int, search: str or None, user_id: int or None, rubric_ids: list[int] or None) -> dict:
        companies = self.company_repository.get_all(limit=limit, offset=offset, search=search, user_id=user_id, rubric_ids=rubric_ids)
        return self.response_ok([{
                'id': company.id,
                'title': company.title,
                'short_description': company.short_description,
                'rubrics': self.get_array_items(company.rubrics),
                'user_count': len(company.users),
                'image': self.get_dict_items(company.image) if company.image else None
            } for company in companies])
