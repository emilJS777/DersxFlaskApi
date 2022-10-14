from src.__Parents.Controller import Controller
from .CategoryRepository import CategoryRepository
from .CategoryService import CategoryService


class CategoryController(Controller):
    category_service: CategoryService = CategoryService(CategoryRepository())

    def post(self) -> dict:
        res: dict = self.category_service.create(self.request.get_json())
        return res

    def put(self) -> dict:
        res: dict = self.category_service.update(self.id, self.request.get_json())
        return res

    def delete(self) -> dict:
        res: dict = self.category_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.category_service.get_by_id(self.id)
        else:
            res: dict = self.category_service.get_all(rubric_id=self.arguments.get('rubric_id'))
        return res
