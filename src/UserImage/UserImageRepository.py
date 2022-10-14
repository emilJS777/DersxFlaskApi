from .UserImageModel import UserImage
from .IUserImageRepo import IUserImageRepo
from flask import g


class UserImageRepository(IUserImageRepo):
    def create(self, filename: str):
        user_image: UserImage = UserImage()
        user_image.user_id = g.user_id
        user_image.filename = filename
        user_image.save_db()

    def delete(self, user_image: UserImage):
        user_image.delete_db()

    def get_by_id(self, user_image_id: int) -> UserImage:
        user_image: UserImage = UserImage.query.filter_by(id=user_image_id).first()
        return user_image

    def get_by_filename(self, filename: str) -> UserImage:
        user_image: UserImage = UserImage.query.filter_by(filename=filename).first()
        return user_image
