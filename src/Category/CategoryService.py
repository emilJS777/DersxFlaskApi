from src.__Parents.Service import Service
from src.__Parents.Repository import Repository
from .ICategoryRepo import ICategoryRepo


class CategoryService(Service, Repository):

    def __init__(self, category_repository: ICategoryRepo):
        self.category_repository: ICategoryRepo = category_repository

    def create(self, body: dict) -> dict:
        self.category_repository.create(body)
        return self.response_created('категория была создано')

    def update(self, category_id: int, body: dict) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found('категория не найдена')
        self.category_repository.update(category=category, body=body)
        return self.response_updated('категория обновлена')

    def delete(self, category_id: int) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found('категория не найдена')
        self.category_repository.delete(category)
        return self.response_deleted('категория была удалена')

    def get_by_id(self, category_id: int) -> dict:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            return self.response_not_found('категория не найдена')
        return self.response_ok({
            'id': category.id,
            'title': category.title,
            'description': category.description
        })

    def get_all(self, rubric_id: int or None) -> dict:
        categories = self.category_repository.get_all(rubric_id=rubric_id)
        return self.response_ok(self.get_array_items(categories))
