import os
from src import app
from .IImageRepo import IImageRepo
from ..__Parents.Service import Service
from flask import g
from datetime import datetime
from flask import send_file, send_from_directory, make_response


class ImageService(Service):
    def __init__(self, image_repository: IImageRepo):
        self.image_repository: IImageRepo = image_repository

    def create(self, image, user_id: int or None, service_id: int or None, publication_id: int or None, company_id: int or None) -> dict:
        self.image_repository.create(
            image=image,
            user_id=user_id,
            service_id=service_id,
            publication_id=publication_id,
            company_id=company_id)

        return self.response_created('данные загружены')

    def delete(self, filename: str = None) -> dict:
        image = self.image_repository.get(filename=filename)
        if not image or not image.creator_id == g.user_id:
            return self.response_not_found('изображение не найдено')

        self.image_repository.delete(image)
        return self.response_deleted('изображение удалено')

    def get(self, filename: str):
        return send_file('../'+app.config["IMAGE_UPLOADS"]+'/'+filename,
                         mimetype=None,
                         as_attachment=False,
                         attachment_filename=None,
                         add_etags=True,
                         cache_timeout=None,
                         conditional=False)
        # return send_file(app.config["IMAGE_UPLOADS"]+'/'+filename, mimetype="image/jpeg")
