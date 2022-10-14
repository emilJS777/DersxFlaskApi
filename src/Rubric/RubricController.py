from src.__Parents.Controller import Controller
from .RubricRepository import RubricRepository
from .RubricService import RubricService


class RubricController(Controller):
    rubric_service: RubricService = RubricService(RubricRepository())

    def post(self) -> dict:
        res: dict = self.rubric_service.create(self.request.get_json())
        return res

    def put(self) -> dict:
        res: dict = self.rubric_service.update(self.id, self.request.get_json())
        return res

    def delete(self) -> dict:
        res: dict = self.rubric_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.rubric_service.get_by_id(self.id)
        else:
            res: dict = self.rubric_service.get_all()
        return res
