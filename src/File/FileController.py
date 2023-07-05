import urllib.parse

from src.__Parents.Controller import Controller
from .FileService import FileService
from .FileRepository import FileRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class FileController(Controller):
    file_service: FileService = FileService(FileRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.file_service.create(
            file=self.request.files['file'],
            offer_id=self.arguments.get("offer_id"))
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.file_service.delete(self.arguments.get("filename"))
        return res

    # @AuthMiddleware.check_authorize
    def get(self):
        filename = self.arguments.get("filename")
        filename = filename.replace(" ", "+")
        res = self.file_service.get(filename=filename)
        return res
