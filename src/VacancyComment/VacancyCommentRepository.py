from sqlalchemy import desc

from .IVacancyCommentRepo import  IVacancyCommentRepo
from .VacancyCommentModel import VacancyComment
from flask import g


class VacancyCommentRepository(IVacancyCommentRepo):
    def create(self, body: dict):
        vacancy_comment: VacancyComment = VacancyComment()
        vacancy_comment.text = body['text']
        vacancy_comment.user_id = g.user_id
        vacancy_comment.vacancy_id = body['vacancy_id']
        vacancy_comment.save_db()

    def update(self, vacancy_comment: VacancyComment, body: dict):
        vacancy_comment.text = body['text']
        vacancy_comment.update_db()

    def delete(self, vacancy_comment: VacancyComment):
        vacancy_comment.delete_db()

    def delete_all(self, vacancy_id: int):
        VacancyComment.query.filter_by(vacancy_id=vacancy_id).delete()

    def get_by_id(self, vacancy_comment_id: int) -> VacancyComment:
        vacancy_comment: VacancyComment() = VacancyComment.query.filter_by(id=vacancy_comment_id).first()
        return vacancy_comment

    def get_all(self, page: int, per_page: int, vacancy_id: int) -> list[VacancyComment]:
        vacancy_comment: list[VacancyComment] = VacancyComment.query.filter_by(vacancy_id=vacancy_id)\
            .order_by(-VacancyComment.creation_date)\
            .paginate(page=page, per_page=per_page)
        return vacancy_comment
