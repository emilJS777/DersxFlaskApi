from .IPublicationCommentRepo import IPublicationCommentRepo
from .PublicationCommentModel import PublicationComment
from flask import g


class PublicationCommentRepository(IPublicationCommentRepo):
    def create(self, body: dict) -> PublicationComment:
        publication_comment: PublicationComment = PublicationComment()
        publication_comment.publication_id = body['publication_id']
        publication_comment.creator_id = g.user_id
        publication_comment.text = body['text']
        publication_comment.save_db()
        return publication_comment

    def update(self, publication_comment: PublicationComment, body: dict):
        publication_comment.text = body['text']
        publication_comment.update_db()

    def delete(self, publication_comment: PublicationComment):
        publication_comment.delete_db()

    def get_by_id(self, publication_comment_id: int) -> PublicationComment:
        publication_comment: PublicationComment = PublicationComment.query.filter_by(id=publication_comment_id).first()
        return publication_comment

    def get_all(self, limit: int, offset: int, publication_id: int) -> list[PublicationComment]:
        publication_comments: list[PublicationComment] = PublicationComment.query\
            .filter_by(publication_id=publication_id)\
            .limit(limit).offset(offset).all()
        return publication_comments
