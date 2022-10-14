from .IUserAboutRepo import IUserAboutRepo
from .UserAboutModel import UserAbout
from flask import g


class UserAboutRepository(IUserAboutRepo):

    def create(self, body: dict):
        user_about: UserAbout = UserAbout()
        user_about.description = body['description']
        user_about.user_id = g.user_id
        user_about.save_db()

    def update(self, user_about: UserAbout, body: dict):
        user_about.description = body['description']
        user_about.update_db()

    def delete(self, user_about: UserAbout):
        user_about.delete_db()

    def get_by_id(self, user_about_id: int) -> UserAbout:
        user_about: UserAbout = UserAbout.query.filter_by(id=user_about_id).first()
        return user_about

    def get_all(self, user_id: int) -> list[UserAbout]:
        user_abouts: list[UserAbout] = UserAbout.query.filter_by(user_id=user_id).all()
        return user_abouts
