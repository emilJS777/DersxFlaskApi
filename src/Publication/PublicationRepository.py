from .IPublicationRepo import IPublicationRepo
from .PublicationModel import Publication
from flask import g


class PublicationRepository(IPublicationRepo):

    def create(self, body: dict) -> Publication:
        publication: Publication = Publication()
        publication.description = body['description']
        publication.creator_id = g.user_id
        publication.save_db()
        return publication

    def update(self, publication: Publication, body: dict):
        publication.description = body['description']
        publication.update_db()

    def delete(self, publication: Publication):
        publication.delete_db()

    def get_by_id(self, publication_id: int) -> Publication:
        publication: Publication = Publication.query.filter_by(id=publication_id).first()
        return publication

    def get_all(self, limit: int, offset: int, creator_id: int or None = None) -> list[Publication]:
        publications: list[Publication] = Publication.query\
            .order_by(-Publication.creation_date)\
            .filter(Publication.creator_id == creator_id if creator_id else Publication.id.isnot(None))\
            .limit(limit).offset(offset).all()
        return publications