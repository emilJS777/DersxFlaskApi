from .IPublicationLikeRepo import IPublicationLikeRepo
from .PublicationLikeModel import PublicationLike
from flask import g
from cachetools import cached, TTLCache
from src import app


class PublicationLikeRepository(IPublicationLikeRepo):
    cache = TTLCache(maxsize=app.config['CACHE_SIZE'], ttl=app.config['CACHE_TTL'])

    def create(self, body: dict):
        publication_like: PublicationLike = PublicationLike()
        publication_like.publication_id = body['publication_id']
        publication_like.user_id = g.user_id
        publication_like.save_db()

    def delete(self, publication_like: PublicationLike):
        publication_like.delete_db()

    @cached(cache)
    def get(self, publication_like_id: int or None = None, publication_id: int or None = None, user_id: int or None = None) -> PublicationLike:
        publication_like: PublicationLike = PublicationLike.query.filter(
            PublicationLike.id == publication_like_id if publication_like_id else PublicationLike.id.isnot(None),
            PublicationLike.publication_id == publication_id if publication_id else PublicationLike.id.isnot(None),
            PublicationLike.user_id == user_id if user_id else PublicationLike.id.isnot(None)
        ).first()
        return publication_like
