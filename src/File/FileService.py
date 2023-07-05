from src import app
from .IFileRepo import IFileRepo
from ..__Parents.Service import Service
from flask import g
from flask import send_file, send_from_directory


class FileService(Service):
    def __init__(self, file_repository: IFileRepo):
        self.file_repository: IFileRepo = file_repository

    def create(self, file, offer_id: int = None) -> dict:
        self.file_repository.create(
            file=file,
            offer_id=offer_id)
        return self.response_created(msg_rus='данные отправлены',
                                     msg_arm='տվյալները ուղարկվել էն',
                                     msg_eng='data sent')

    def delete(self, filename: str = None) -> dict:
        file = self.file_repository.get(filename=filename)
        self.file_repository.delete(file)
        return self.response_deleted(msg_rus='данные удалены',
                                     msg_eng='data removed',
                                     msg_arm='տվյալները հեռացված է')

    def get(self, filename: str):
        return send_file('../'+app.config["FILE_UPLOADS"]+'/'+filename,
                         mimetype=None,
                         as_attachment=False,
                         conditional=False)