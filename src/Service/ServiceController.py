import ast
from src.__Parents.Controller import Controller
from .ServiceService import ServiceService
from .ServiceRepository import ServiceRepository
from src.Category.CategoryRepository import CategoryRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .ServiceValidator import service_schema
from src.ServiceImage.ServiceImageRepository import ServiceImageRepository


class ServiceController(Controller):
    service_service: ServiceService = ServiceService(ServiceRepository(), CategoryRepository(), ServiceImageRepository())

    @expects_json(service_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.service_service.create(body=self.request.get_json())
        return res

    @expects_json(service_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.service_service.update(service_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.service_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.service_service.get_by_id(self.id)
        else:
            res: dict = self.service_service.get_all(
                page=self.page,
                per_page=self.per_page,
                search=self.arguments.get('search') or None,
                rubric_id=self.arguments.get('rubric_id') or None,
                category_ids=ast.literal_eval(self.arguments.get('category_ids')) if self.arguments.get('category_ids') else None,
                creator_id=self.arguments.get('creator_id'))
        return res

