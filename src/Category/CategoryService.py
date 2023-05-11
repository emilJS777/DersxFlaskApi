from src.__Parents.Service import Service
from src.__Parents.Repository import Repository
from .ICategoryRepo import ICategoryRepo


class CategoryService(Service, Repository):

    def __init__(self, category_repository: ICategoryRepo):
        self.category_repository: ICategoryRepo = category_repository

    def create(self, body: dict) -> dict:
        self.category_repository.create(body)
        return self.response_created(msg_rus='категория была создано',
                                     msg_arm='կատեգորիան ստեղծված է',
                                     msg_eng='category has been created')

    def update(self, category_id: int, body: dict) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found(msg_rus='категория не найдена',
                                           msg_eng='category not found',
                                           msg_arm='կատեգորիան չի գտնվել')

        self.category_repository.update(category=category, body=body)
        return self.response_updated(msg_rus='категория обновлена',
                                     msg_eng='category updated',
                                     msg_arm='կատեգորիան թարմացված է')

    def delete(self, category_id: int) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found(msg_rus='категория не найдена',
                                           msg_eng='category not found',
                                           msg_arm='կատեգորիան չի գտնվել')
        self.category_repository.delete(category)
        return self.response_deleted(msg_rus='категория была удалена',
                                     msg_arm='կատեգորիան ջնջված է',
                                     msg_eng='category deleted')

    def get_by_id(self, category_id: int) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found(msg_rus='категория не найдена',
                                           msg_eng='category not found',
                                           msg_arm='կատեգորիան չի գտնվել')
        return self.response_ok({
            'id': category.id,
            'title': category.title,
            'description': category.description
        })

    def get_all(self, rubric_id: int or None) -> dict:
        categories = self.category_repository.get_all(rubric_id=rubric_id)
        return self.response_ok(self.get_array_items(categories))
