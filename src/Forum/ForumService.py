from .IForumRepo import IForumRepo
from src.ForumDiscussion.IForumDiscussionRepo import IForumDiscussionRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class ForumService(Service, Repository):

    def __init__(self, forum_repository: IForumRepo, forum_discussion_repository: IForumDiscussionRepo):
        self.forum_repository: IForumRepo = forum_repository
        self.forum_discussion_repository: IForumDiscussionRepo = forum_discussion_repository

    def create(self, body: dict) -> dict:
        self.forum_repository.create(body=body)
        return self.response_created('форум создан')

    def update(self, forum_id: int, body: dict) -> dict:
        forum = self.forum_repository.get_by_id(forum_id)
        if not forum or not forum.creator_id == g.user_id:
            return self.response_not_found('форум не найден')
        self.forum_repository.update(forum=forum, body=body)
        return self.response_updated('форум обновлен')

    def delete(self, forum_id: int) -> dict:
        forum = self.forum_repository.get_by_id(forum_id)
        if not forum or not forum.creator_id == g.user_id:
            return self.response_not_found('форум не найден')

        self.forum_discussion_repository.delete_all(forum_id)
        self.forum_repository.delete(forum)
        return self.response_deleted('форум удален')

    def get_by_id(self, forum_id: int) -> dict:
        forum = self.forum_repository.get_by_id(forum_id)
        if not forum:
            return self.response_not_found('форум не найден')
        return self.response_ok({
            'id': forum.id,
            'title': forum.title,
            'topic': forum.topic,
            'forum_discussion_count': len(forum.forum_discussions),
            'rubric': self.get_dict_items(forum.rubric),
            'creation_date': forum.creation_date.strftime("%Y-%m-%d"),
            'creator': {
                'id': forum.creator.id,
                'name': forum.creator.name,
                'first_name': forum.creator.first_name,
                'last_name': forum.creator.last_name,
                'image': self.get_encode_image(forum.creator.image.filename) if forum.creator.image else None
            }
        })

    def get_all(self, page: int, per_page: int, rubric_id: int or None, search: str or None, creator_id: int or None) -> dict:
        forums = self.forum_repository.get_all(
            page=page,
            per_page=per_page,
            rubric_id=rubric_id,
            search=search,
            creator_id=creator_id)
        return self.response_ok({'total': forums.total,
                                 'page': forums.page,
                                 'pages': forums.pages,
                                 'per_page': forums.per_page,
                                 'items': [{
                                     'id': forum.id,
                                     'title': forum.title,
                                     'topic': forum.topic,
                                     'forum_discussion_count': len(forum.forum_discussions),
                                     'rubric': self.get_dict_items(forum.rubric),
                                     'creator_id': forum.creator_id,
                                     'creation_date': forum.creation_date.strftime("%Y-%m-%d"),
                                     'creator': {
                                         'name': forum.creator.name,
                                         'first_name': forum.creator.first_name,
                                         'last_name': forum.creator.last_name,
                                         'image': self.get_encode_image(forum.creator.image.filename) if forum.creator.image.filename else None
                                     }
                                 } for forum in forums.items]})
