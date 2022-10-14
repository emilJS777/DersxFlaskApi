from .IWorkExperienceRepo import IWorkExperienceRepo
from .WorkExperienceModel import WorkExperience
from flask import g


class WorkExperienceRepository(IWorkExperienceRepo):
    def create(self, body: dict):
        work_experience: WorkExperience = WorkExperience()
        work_experience.title = body['title']
        work_experience.description = body['description']
        work_experience.skills = body['skills']
        work_experience.link = body['link']
        work_experience.date_start = body['date_start'].split('T')[0] or None
        work_experience.date_end = body['date_end'].split('T')[0] or None
        work_experience.user_id = g.user_id
        work_experience.save_db()

    def update(self, work_experience: WorkExperience, body: dict):
        work_experience.title = body['title']
        work_experience.description = body['description']
        work_experience.skills = body['skills']
        work_experience.link = body['link']
        work_experience.date_start = body['date_start'].split('T')[0] or None
        work_experience.date_end = body['date_end'].split('T')[0] or None
        work_experience.update_db()

    def delete(self, work_experience: WorkExperience):
        work_experience.delete_db()

    def get_by_id(self, work_experience_id: int):
        work_experience: WorkExperience = WorkExperience.query.filter_by(id=work_experience_id).first()
        return work_experience

    def get_all(self, user_id: int):
        work_experiences: list[WorkExperience] = WorkExperience.query.filter_by(user_id=user_id).all()
        return work_experiences
