from sqlalchemy import or_
from .IForumRepo import IForumRepo
from .ForumModel import Forum
from flask import g


class ForumRepository(IForumRepo):
    def create(self, body: dict):
        forum: Forum = Forum()
        forum.title = body['title']
        forum.topic = body['topic']
        forum.rubric_id = body['rubric_id']
        forum.creator_id = g.user_id
        forum.save_db()

    def update(self, forum: Forum, body: dict):
        forum.title = body['title']
        forum.topic = body['topic']
        forum.rubric_id = body['rubric_id']
        forum.update_db()

    def delete(self, forum: Forum):
        forum.delete_db()

    def get_by_id(self, forum_id: int) -> Forum:
        forum: Forum = Forum.query.filter_by(id=forum_id).first()
        return forum

    def get_all(self, page: int, per_page: int, rubric_id: int or None, search: str or None, creator_id: int or None):
        forums = Forum.query.filter(Forum.creator_id == creator_id if creator_id else Forum.id.isnot(None),
                                    Forum.rubric_id == rubric_id if rubric_id else Forum.id.isnot(None),
                                    or_(Forum.title.like(f"%{search}%"), Forum.topic.like(f"%{search}%")) if search else Forum.id.isnot(None))\
            .order_by(-Forum.creation_date)\
            .paginate(page=page, per_page=per_page)
        return forums
