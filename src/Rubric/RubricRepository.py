from src.Rubric.IRubricRepo import IRubricRepo
from .RubricModel import Rubric


class RubricRepository(IRubricRepo):

    def create(self, body: dict):
        rubric = Rubric()
        rubric.title = body['title']
        rubric.description = body['description']
        rubric.save_db()

    def update(self, rubric: Rubric, body: dict):
        rubric.title = body['title']
        rubric.description = body['description']
        rubric.update_db()

    def delete(self, rubric: Rubric):
        rubric.delete_db()

    def get_by_id(self, rubric_id: int) -> Rubric:
        rubric: Rubric = Rubric.query.filter_by(id=rubric_id).first()
        return rubric

    def get_all(self) -> list[Rubric]:
        rubric: list[Rubric] = Rubric.query.all()
        return rubric
