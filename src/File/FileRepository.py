import os
from src import app
from .IFileRepo import IFileRepo
from .FileModel import File
from flask import g
from datetime import datetime


class FileRepository(IFileRepo):

    def create(self, file, offer_id: int = None):
        filename = f"{g.user_id}{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}{file.filename}"
        file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
        file: File = File()
        file.filename = filename
        file.vacancy_offer_id = offer_id
        file.save_db()

    def delete(self, file: File):
        os.remove(app.config["FILE_UPLOADS"] + '/' + file.filename)
        file.delete_db()

    def get(self, filename: str) -> File:
        image: File = File.query.filter_by(filename=filename).first()
        return image
