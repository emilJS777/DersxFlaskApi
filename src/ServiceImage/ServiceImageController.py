from src.__Parents.Controller import Controller
from .ServiceImageService import ServiceImageService
from .ServiceImageRepository import ServiceImageRepository
from src.Service.ServiceRepository import ServiceRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class ServiceImageController(Controller):
    service_image_service: ServiceImageService = ServiceImageService(ServiceImageRepository(), ServiceRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.service_image_service.create(service_id=int(self.arguments.get('service_id')), image=self.request.files['image'])
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.service_image_service.delete(int(self.arguments.get('service_id')))
        return res
