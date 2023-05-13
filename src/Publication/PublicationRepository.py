from .IPublicationRepo import IPublicationRepo
from .PublicationModel import Publication
from src.PublicationLike.PublicationLikeModel import PublicationLike
from flask import g
from src import app
from cachetools import cached, TTLCache


class PublicationRepository(IPublicationRepo):
    cache = TTLCache(maxsize=app.config['CACHE_SIZE'], ttl=app.config['CACHE_TTL'])

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

    @cached(cache)
    def get_all(self, limit: int, offset: int, creator_id: int or None = None, liked_id: int or None = None) -> list[Publication]:
        publications: list[Publication] = Publication.query\
            .order_by(-Publication.creation_date) \
            .filter(Publication.creator_id == creator_id if creator_id else Publication.id.isnot(None)) \
            .where(Publication.likes.any(PublicationLike.user_id.in_([liked_id])) if liked_id else Publication.id.isnot(None)) \
            .limit(limit).offset(offset).all()
        return publications
