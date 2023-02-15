import ast

from src.__Parents.Controller import Controller
from .CompanyService import CompanyService
from .CompanyRepository import CompanyRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .CompanyValidator import company_schema
from src.Rubric.RubricRepository import RubricRepository


class CompanyController(Controller):
    company_service: CompanyService = CompanyService(CompanyRepository(), RubricRepository())

    @expects_json(company_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.company_service.create(self.request.get_json())
        return res

    @expects_json(company_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.company_service.update(company_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.company_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.company_service.get_by_id(self.id)
        else:
            res: dict = self.company_service.get_all(limit=self.arguments.get('limit'),
                                                     offset=self.arguments.get('offset'),
                                                     search=self.arguments.get("search"),
                                                     user_id=self.arguments.get('user.id'),
                                                     rubric_ids=ast.literal_eval(self.arguments.get('rubric_ids')) if self.arguments.get('rubric_ids') else None)
        return res
