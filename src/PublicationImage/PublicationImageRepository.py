from .IPublicationImageRepo import IPublicationImageRepo
from .PublicationImageModel import PublicationImage


class PublicationImageRepository(IPublicationImageRepo):
    def create(self, filename: str, publication_id: int):
        publication_image: PublicationImage = PublicationImage()
        publication_image.filename = filename
        publication_image.publication_id = publication_id
        publication_image.save_db()

    def update(self, publication_image: PublicationImage, filename: str):
        publication_image.filename = filename
        publication_image.update_db()

    def delete(self, publication_image: PublicationImage):
        publication_image.delete_db()

    def get_by_id(self, publication_image_id: int) -> PublicationImage:
        publication_image: PublicationImage = PublicationImage.query.filter_by(id=publication_image_id).first()
        return publication_image

    def get_by_filename(self, filename: str) -> PublicationImage:
        publication_image: PublicationImage = PublicationImage.query.filter_by(filename=filename).first()
        return publication_image
