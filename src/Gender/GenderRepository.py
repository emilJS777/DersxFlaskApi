from .IGenderRepo import IGenderRepo
from .GenderModel import Gender


class GenderRepository(IGenderRepo):

    def create(self, body: dict):
        gender: Gender = Gender()
        gender.title = body['title']
        gender.save_db()

    def update(self, gender: Gender, body: dict):
        gender.title = body['title']
        gender.update_db()

    def delete(self, gender: Gender):
        gender.delete_db()

    def get_by_id(self, gender_id: int) -> Gender:
        gender: Gender = Gender.query.filter_by(id=gender_id).first()
        return gender

    def get_all(self) -> list[Gender]:
        genders: list[Gender] = Gender.query.all()
        return genders
