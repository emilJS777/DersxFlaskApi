from .IServiceImageRepo import IServiceImageRepo
from .ServiceImageModel import ServiceImage


class ServiceImageRepository(IServiceImageRepo):
    def create(self, filename: str, service_id: int):
        service_image: ServiceImage = ServiceImage()
        service_image.filename = filename
        service_image.service_id = service_id
        service_image.save_db()

    def update(self, service_image: ServiceImage, filename: str):
        service_image.filename = filename
        service_image.update_db()

    def delete(self, service_image: ServiceImage):
        service_image.delete_db()

    def get_by_id(self, service_image_id: int) -> ServiceImage:
        service_image: ServiceImage = ServiceImage.query.filter_by(id=service_image_id).first()
        return service_image

    def get_by_filename(self, filename: str) -> ServiceImage:
        service_image: ServiceImage = ServiceImage.query.filter_by(filename=filename).first()
        return service_image
