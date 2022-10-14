from .GenderService import GenderService
from .GenderRepository import GenderRepository
from ..__Parents.Controller import Controller


class GenderController(Controller):
    gender_service: GenderService = GenderService(GenderRepository())

    def post(self) -> dict:
        res: dict = self.gender_service.create(self.request.get_json())
        return res

    def put(self) -> dict:
        res: dict = self.gender_service.update(gender_id=self.id, body=self.request.get_json())
        return res

    def delete(self) -> dict:
        res: dict = self.gender_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.gender_service.get_by_id(self.id)
        else:
            res: dict = self.gender_service.get_all()
        return res
