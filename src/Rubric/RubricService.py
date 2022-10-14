from src.__Parents.Service import Service
from src.__Parents.Repository import Repository
from .IRubricRepo import IRubricRepo


class RubricService(Service, Repository):

    def __init__(self, rubric_repository: IRubricRepo):
        self.rubric_repository: IRubricRepo = rubric_repository

    def create(self, body: dict) -> dict:
        self.rubric_repository.create(body)
        return self.response_created('рубрика была создано')

    def update(self, rubric_id: int, body: dict) -> dict:
        rubric = self.rubric_repository.get_by_id(rubric_id)
        if not rubric:
            return self.response_not_found('рубрика не найдена')
        self.rubric_repository.update(rubric=rubric, body=body)
        return self.response_updated('рубрика обновлена')

    def delete(self, rubric_id: int) -> dict:
        rubric = self.rubric_repository.get_by_id(rubric_id)
        if not rubric:
            return self.response_not_found('рубрика не найдена')
        self.rubric_repository.delete(rubric)
        return self.response_deleted('рубрика была удалена')

    def get_by_id(self, rubric_id: int) -> dict:
        rubric = self.rubric_repository.get_by_id(rubric_id)
        if not rubric:
            return self.response_not_found('рубрика не найдена')
        return self.response_ok({
            'id': rubric.id,
            'title': rubric.title,
            'description': rubric.description
        })

    def get_all(self) -> dict:
        rubrics = self.rubric_repository.get_all()
        return self.response_ok(self.get_array_items(rubrics))
