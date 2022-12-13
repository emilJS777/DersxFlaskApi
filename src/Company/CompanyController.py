from src.__Parents.Controller import Controller
from .CompanyService import CompanyService
from .CompanyRepository import CompanyRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .CompanyValidator import company_schema


class CompanyController(Controller):
    company_service: CompanyService = CompanyService(CompanyRepository())

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

    def get(self) -> dict:
        if self.id:
            res: dict = self.company_service.get_by_id(self.id)
        else:
            res: dict = self.company_service.get_all(page=self.page, per_page=self.per_page, search=self.arguments.get("search"))
        return res
