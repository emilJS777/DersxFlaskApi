from src.__Parents.Service import Service
from .IVacancyRepo import IVacancyRepo
from src.Category.ICategoryRepo import ICategoryRepo
from src.VacancyOffer.IVacancyOfferRepo import IVacancyOfferRepo
from src.VacancyComment.IVacancyCommentRepo import IVacancyCommentRepo
from flask import g
from ..__Parents.Repository import Repository


class VacancyService(Service, Repository):
    def __init__(self, vacancy_repository: IVacancyRepo,
                 category_repository: ICategoryRepo,
                 vacancy_offer_repository: IVacancyOfferRepo,
                 vacancy_comment_repository: IVacancyCommentRepo):
        self.vacancy_repository: IVacancyRepo = vacancy_repository
        self.category_repository: ICategoryRepo = category_repository
        self.vacancy_offer_repository: IVacancyOfferRepo = vacancy_offer_repository
        self.vacancy_comment_repository: IVacancyCommentRepo = vacancy_comment_repository

    def create(self, body: dict) -> dict:
        categories: list = self.category_repository.get_all(ids=body['category_ids'])
        self.vacancy_repository.create(body=body, categories=categories)
        return self.response_created('вакансия создана')

    def update(self, vacancy_id: int, body: dict) -> dict:
        vacancy = self.vacancy_repository.get_by_id(vacancy_id)
        if not vacancy:
            return self.response_not_found('вакансия не найдена')
        categories: list = self.category_repository.get_all(ids=body['category_ids'])
        self.vacancy_repository.update(vacancy=vacancy, body=body, categories=categories)
        return self.response_updated('вакансия обновлена')

    def delete(self, vacancy_id: int) -> dict:
        vacancy = self.vacancy_repository.get_by_id(vacancy_id)
        if not vacancy or not vacancy.creator_id == g.user_id:
            return self.response_not_found('вакансия не найдена')

        self.vacancy_offer_repository.delete_all(vacancy_id)
        self.vacancy_comment_repository.delete_all(vacancy_id)
        self.vacancy_repository.delete(vacancy)
        return self.response_deleted('вакансия удалена')

    def get_by_id(self, vacancy_id: int) -> dict:
        vacancy = self.vacancy_repository.get_by_id(vacancy_id)
        if not vacancy:
            return self.response_not_found('вакансия не найдена')
        vacancy.categories = vacancy.categories
        vacancy.payment_interval = vacancy.payment_interval
        return self.response_ok({
            'id': vacancy.id,
            'title': vacancy.title,
            'long_description': vacancy.long_description,
            'short_description': vacancy.short_description,
            "price": vacancy.price,
            "rubric": self.get_dict_items(vacancy.rubric),
            "categories": self.get_array_items(vacancy.categories),
            "payment_interval_id": vacancy.payment_interval_id,
            "creation_date": vacancy.creation_date,
            "creator_id": vacancy.creator_id,
            'vacancy_offers_count': len(vacancy.vacancy_offers),
            'vacancy_comments_count': len(vacancy.vacancy_comments),
            "creator": {
                "id": vacancy.creator.id,
                "name": vacancy.creator.name,
                "first_name": vacancy.creator.first_name,
                "last_name": vacancy.creator.last_name,
                "image": self.get_encode_image(vacancy.creator.image.filename) if vacancy.creator.image else None
            },
        })

    def get_all(self, page: int, per_page: int, search: str or None, rubric_id: int or None, creator_id: int or None,
                payment_interval_ids: list[int], category_ids: list[int], price_start: float, price_end: float) -> dict:
        vacancies = self.vacancy_repository.get_all(
            page=page,
            per_page=per_page,
            search=search,
            rubric_id=rubric_id,
            creator_id=creator_id,
            payment_interval_ids=payment_interval_ids,
            category_ids=category_ids,
            price_start=price_start,
            price_end=price_end)

        return self.response_ok({
            'total': vacancies.total,
            'page': vacancies.page,
            'pages': vacancies.pages,
            'per_page': vacancies.per_page,
            'items': [{
                "id": vacancy.id,
                "title": vacancy.title,
                "short_description": vacancy.short_description,
                "price": vacancy.price,
                "rubric": self.get_dict_items(vacancy.rubric),
                "categories": self.get_array_items(vacancy.categories),
                "payment_interval": self.get_dict_items(vacancy.payment_interval),
                "creation_date": vacancy.creation_date,
                "creator_id": vacancy.creator_id,
                "creator": {
                    "id": vacancy.creator.id,
                    "name": vacancy.creator.name,
                    "first_name": vacancy.creator.first_name,
                    "last_name": vacancy.creator.last_name,
                    "image": self.get_encode_image(vacancy.creator.image.filename) if vacancy.creator.image else None
                },
                'vacancy_offers_count': len(vacancy.vacancy_offers),
            } for vacancy in vacancies.items ] })
