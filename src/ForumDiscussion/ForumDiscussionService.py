from .IForumDiscussionRepo import IForumDiscussionRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class ForumDiscussionService(Service, Repository):
    def __init__(self, forum_discussion_repository: IForumDiscussionRepo):
        self.forum_discussion_repository: IForumDiscussionRepo = forum_discussion_repository

    def create(self, body: dict) -> dict:
        self.forum_discussion_repository.create(body)
        return self.response_created('обсуждение создано')

    def update(self, forum_discussion_id: int, body: dict) -> dict:
        forum_discussion = self.forum_discussion_repository.get_by_id(forum_discussion_id)
        if not forum_discussion or not forum_discussion.creator_id == g.user_id:
            return self.response_not_found('обсуждение не найдено')
        self.forum_discussion_repository.update(forum_discussion=forum_discussion, body=body)
        return self.response_updated('обсуждение обновлено')

    def delete(self, forum_discussion_id: int) -> dict:
        forum_discussion = self.forum_discussion_repository.get_by_id(forum_discussion_id)
        if not forum_discussion or not forum_discussion.creator_id == g.user_id:
            return self.response_not_found('обсуждение не найдено')
        self.forum_discussion_repository.delete(forum_discussion)
        return self.response_deleted('обсуждение удалено')

    def get_by_id(self, forum_discussion_id: int) -> dict:
        forum_discussion = self.forum_discussion_repository.get_by_id(forum_discussion_id)
        if not forum_discussion:
            return self.response_not_found('обсуждение не найдено')
        return self.response_ok(self.get_dict_items(forum_discussion))

    def get_all(self, forum_id: int) -> dict:
        forum_discussions = self.forum_discussion_repository.get_all(forum_id=forum_id)
        return self.response_ok([{
            'id': forum_discussion.id,
            'description': forum_discussion.description,
            'creation_date': forum_discussion.creation_date.strftime("%Y-%m-%d"),
            'creator': {
                'id': forum_discussion.creator.id,
                'name': forum_discussion.creator.name,
                'first_name': forum_discussion.creator.first_name,
                'last_name': forum_discussion.creator.last_name,
                'image': self.get_dict_items(forum_discussion.creator.image) if forum_discussion.creator.image else None
            }
        } for forum_discussion in forum_discussions])
