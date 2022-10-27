from .IForumDiscussionRepo import IForumDiscussionRepo
from .ForumDiscussionModel import ForumDiscussion
from flask import g


class ForumDiscussionRepository(IForumDiscussionRepo):

    def create(self, body: dict):
        forum_discussion: ForumDiscussion = ForumDiscussion()
        forum_discussion.description = body['description']
        forum_discussion.forum_id = body['forum_id']
        forum_discussion.creator_id = g.user_id
        forum_discussion.save_db()

    def update(self, forum_discussion: ForumDiscussion, body: dict):
        forum_discussion.description = body['description']
        forum_discussion.update_db()

    def delete(self, forum_discussion: ForumDiscussion):
        forum_discussion.delete_db()

    def delete_all(self, forum_id: int):
        ForumDiscussion.query.filter_by(forum_id=forum_id).delete()

    def get_by_id(self, forum_discussion_id: int) -> ForumDiscussion:
        forum_discussion: ForumDiscussion = ForumDiscussion.query.filter_by(id=forum_discussion_id).first()
        return forum_discussion

    def get_all(self, forum_id: int) -> list[ForumDiscussion]:
        forum_discussions = ForumDiscussion.query.filter_by(forum_id=forum_id).all()
        return forum_discussions
