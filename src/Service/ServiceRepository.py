from sqlalchemy import or_
from src.Category.CategoryModel import Category
from .IServiceRepo import IServiceRepo
from .ServiceModel import Service
from flask import g


class ServiceRepository(IServiceRepo):
    def create(self, body: dict, categories: list) -> Service:
        service: Service = Service()
        service.title = body['title']
        service.short_description = body['short_description']
        service.long_description = body['long_description']
        service.categories = categories
        service.rubric_id = body['rubric_id']
        service.payment_interval_id = body['payment_interval_id']
        service.price = body['price']
        service.creator_id = g.user_id
        service.save_db()
        return service

    def update(self, service: Service, body: dict, categories: list):
        service.title = body['title']
        service.short_description = body['short_description']
        service.long_description = body['long_description']
        service.categories = categories
        service.rubric_id = body['rubric_id']
        service.payment_interval_id = body['payment_interval_id']
        service.price = body['price']
        service.update_db()

    def delete(self, service: Service):
        service.delete_db()

    def get_by_id(self, service_id: int) -> Service:
        service: Service = Service.query.filter_by(id=service_id).first()
        return service

    def get_all(self, page: int, per_page: int, exclude_id: int or None, rubric_id: int or None, category_ids: list or None, payment_interval_ids: list or None,
                search: str or None, creator_id: int or None = None):

        services = Service.query.filter(Service.creator_id == creator_id if creator_id else Service.id.isnot(None),
                                        Service.rubric_id == rubric_id if rubric_id else Service.id.isnot(None),
                                        Service.id != exclude_id if exclude_id else Service.id.isnot(None),
                                        or_(Service.title.like(f"%{search}%"), Service.short_description.like(f"%{search}%")) if search else Service.id.isnot(None)) \
                                        .where(Service.categories.any(Category.id.in_(category_ids)) if category_ids else Service.id.isnot(None)) \
                                        .filter(Service.payment_interval_id.in_(payment_interval_ids) if payment_interval_ids else Service.id.isnot(None))\
            .paginate(page=page, per_page=per_page)
        return services
