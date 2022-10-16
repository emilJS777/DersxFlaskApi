from sqlalchemy import or_, desc
from .IVacancyRepo import IVacancyRepo
from .VacancyModel import Vacancy, VacancyCategory
from flask import g
from ..__Parents.Repository import Repository
from src.Category.CategoryModel import Category


class VacancyRepository(IVacancyRepo, Repository):
    def create(self, body: dict, categories: list):
        vacancy: Vacancy = Vacancy()
        vacancy.title = body['title']
        vacancy.short_description = body['short_description']
        vacancy.long_description = body['long_description']
        vacancy.price = body['price']
        vacancy.rubric_id = body['rubric_id']
        vacancy.categories = categories
        vacancy.payment_interval_id = body['payment_interval_id']
        vacancy.creator_id = g.user_id
        vacancy.save_db()

    def update(self, vacancy: Vacancy, body: dict, categories: list):
        vacancy.title = body['title']
        vacancy.short_description = body['short_description']
        vacancy.long_description = body['long_description']
        vacancy.price = body['price']
        vacancy.rubric_id = body['rubric_id']
        vacancy.categories = categories
        vacancy.payment_interval_id = body['payment_interval_id']
        vacancy.update_db()

    def delete(self, vacancy: Vacancy):
        VacancyCategory.query.filter_by(vacancy_id=vacancy.id).delete()
        vacancy.delete_db()

    def get_by_id(self, vacancy_id: int) -> Vacancy:
        vacancy: Vacancy = Vacancy.query.filter_by(id=vacancy_id).first()
        return vacancy

    def get_all(self, page: int, per_page: int, search: str or None, rubric_id: int or None, creator_id: int or None,
                payment_interval_ids: list[int], category_ids: list, price_start: float, price_end: float):
        vacancies = Vacancy.query\
            .filter(or_(Vacancy.title.like(f"%{search}%"), Vacancy.short_description.like(f"%{search}%")) if search else Vacancy.id.isnot(None))\
            .filter(Vacancy.rubric_id == rubric_id if rubric_id else Vacancy.id.isnot(None))\
            .filter(Vacancy.creator_id == creator_id if creator_id else Vacancy.creator_id.isnot(None))\
            .where(Vacancy.categories.any(Category.id.in_(category_ids)))\
            .filter(Vacancy.payment_interval_id.in_(payment_interval_ids))\
            .order_by(-Vacancy.creation_date)\
            .paginate(page=page, per_page=per_page)
        return vacancies
