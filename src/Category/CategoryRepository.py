from .ICategoryRepo import ICategoryRepo
from .CategoryModel import Category
from cachetools import cached, TTLCache
from src import app


class CategoryRepository(ICategoryRepo):
    cache = TTLCache(maxsize=app.config['CACHE_SIZE'], ttl=app.config['CACHE_TTL'])

    def create(self, body: dict):
        category = Category()
        category.title = body['title']
        category.title_arm = body['title_arm']
        category.title_eng = body['title_eng']
        category.title_rus = body['title_rus']
        category.description = body['description']
        category.rubric_id = body['rubric_id']
        category.save_db()

    def update(self, category: Category, body: dict):
        category.title = body['title']
        category.title_arm = body['title_arm']
        category.title_eng = body['title_eng']
        category.title_rus = body['title_rus']
        category.description = body['description']
        category.update_db()

    def delete(self, category: Category):
        category.delete_db()

    def get_by_id(self, category_id: int) -> Category:
        category: Category = Category.query.filter_by(id=category_id).first()
        return category

    @cached(cache)
    def get_all(self, rubric_id: int or None = None, ids: list[int] or None = None) -> list[Category]:
        category: list[Category] = Category.query.filter(Category.id.in_(ids) if ids is not None else Category.id.isnot(None),
                                                         Category.rubric_id == rubric_id if rubric_id else Category.id.isnot(None)).all()
        return category
