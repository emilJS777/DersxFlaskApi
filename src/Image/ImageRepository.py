import os
from src import app
from .IImageRepo import IImageRepo
from .ImageModel import Image
from flask import g
from datetime import datetime


class ImageRepository(IImageRepo):

    def create(self, image, user_id: int = None, service_id: int = None, publication_id: int = None):
        filename = f"{g.user_id}{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}{image.filename}"
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

        image: Image = Image()
        image.filename = filename
        image.user_id = user_id
        image.service_id = service_id
        image.publication_id = publication_id
        image.creator_id = g.user_id
        image.save_db()

    def delete(self, image: Image):
        os.remove(app.config["IMAGE_UPLOADS"] + '/' + image.filename)
        image.delete_db()

    def get(self, filename: str) -> Image:
        image: Image = Image.query.filter_by(filename=filename).first()
        return image
