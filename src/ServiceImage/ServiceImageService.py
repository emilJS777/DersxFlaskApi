from src.__Parents.Service import Service
from .IServiceImageRepo import IServiceImageRepo
from src.Service.IServiceRepo import IServiceRepo
from flask import g
from datetime import datetime
from src import app
import os


class ServiceImageService(Service):
    def __init__(self, service_image_repository: IServiceImageRepo, service_repository: IServiceRepo):
        self.service_image_repository: IServiceImageRepo = service_image_repository
        self.service_repository: IServiceRepo = service_repository

    def create(self, service_id: int, image) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not  service.creator_id == g.user_id:
            return self.response_not_found(msg_eng='', msg_rus='', msg_arm='')

        filename = f"{g.user_id}{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}{image.filename}"
        image.save(os.path.join(app.config["SERVICE_IMAGE_UPLOADS"], filename))
        self.service_image_repository.create(filename=filename, service_id=service_id)
        return self.response_created(msg_eng='', msg_rus='', msg_arm='')

    def delete(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not service.creator_id == g.user_id:
            return self.response_not_found(msg_eng='', msg_rus='', msg_arm='')

        os.remove(app.config["SERVICE_IMAGE_UPLOADS"] + '/' + service.image.filename)
        self.service_image_repository.delete(service_image=service.image)
        return self.response_deleted(msg_eng='', msg_rus='', msg_arm='')
