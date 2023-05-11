from .IServiceRepo import IServiceRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from datetime import datetime
from src import app
import os
from flask import g
from src.Category.ICategoryRepo import ICategoryRepo
from src.Image.IImageRepo import IImageRepo


class ServiceService(Service, Repository):

    def __init__(self, service_repository: IServiceRepo, category_repository: ICategoryRepo, image_repository: IImageRepo):
        self.service_repository: IServiceRepo = service_repository
        self.category_repository: ICategoryRepo = category_repository
        self.image_repository: IImageRepo = image_repository

    def create(self, body: dict) -> dict:
        service = self.service_repository.create(
                  body=body,
                  categories=self.category_repository.get_all(ids=body['category_ids']))
        return self.response_ok({'id': service.id, 'msg': 'услуга успешно создана'})

    def update(self, service_id: int, body: dict) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not service.creator_id == g.user_id:
            return self.response_updated(msg_eng='', msg_rus='', msg_arm='')
        self.service_repository.update(
            service=service,
            body=body,
            categories=self.category_repository.get_all(ids=body['category_ids']))
        return self.response_updated(msg_eng='', msg_rus='', msg_arm='')

    def delete(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not service.creator_id == g.user_id:
            return self.response_updated(msg_eng='', msg_rus='', msg_arm='')

        if service.image:
            self.image_repository.delete(service.image)

        self.service_repository.delete(service)
        return self.response_deleted(msg_eng='', msg_rus='', msg_arm='')

    def get_by_id(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service:
            return self.response_updated(msg_eng='', msg_rus='', msg_arm='')
        return self.response_ok({
            'id': service.id,
            'title': service.title,
            'short_description': service.short_description,
            'long_description': service.long_description,
            'rubric_id': service.rubric_id,
            'rubric': self.get_dict_items(service.rubric),
            'categories': self.get_array_items(service.categories),
            'payment_interval': self.get_dict_items(service.payment_interval),
            'price': service.price,
            'contacts': self.get_array_items(service.creator.user_contacts),
            'creation_date': service.creation_date.strftime("%Y-%m-%d"),
            'image': self.get_dict_items(service.image) if service.image else None,
            "creator": {
                "id": service.creator.id,
                "name": service.creator.name,
                "first_name": service.creator.first_name,
                "last_name": service.creator.last_name,
                'image': self.get_dict_items(service.creator.image) if service.creator.image else None
            },
        })

    def get_all(self, page: int, per_page: int, exclude_id: int or None, rubric_id: int or None, category_ids: list or None, payment_interval_ids: list or None,
                search: str or None, creator_id: int or None) -> dict:

        services = self.service_repository.get_all(
            page=page,
            per_page=per_page,
            exclude_id=exclude_id,
            rubric_id=rubric_id,
            category_ids=category_ids,
            payment_interval_ids=payment_interval_ids,
            search=search,
            creator_id=creator_id)
        return self.response_ok({
            'total': services.total,
            'page': services.page,
            'pages': services.pages,
            'per_page': services.per_page,
            'items': [{
                'id': service.id,
                'title': service.title,
                'short_description': service.short_description,
                'rubric_id': service.rubric_id,
                'rubric': self.get_dict_items(service.rubric),
                'categories': self.get_array_items(service.categories),
                'payment_interval': self.get_dict_items(service.payment_interval),
                'price': service.price,
                'creation_date': service.creation_date.strftime("%Y-%m-%d"),
                'image': self.get_dict_items(service.image) if service.image else None
            } for service in services.items]
        })
