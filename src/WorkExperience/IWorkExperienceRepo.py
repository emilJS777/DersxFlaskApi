from abc import ABC, abstractmethod
from .WorkExperienceModel import WorkExperience


class IWorkExperienceRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, work_experience: WorkExperience, body: dict):
        pass

    @abstractmethod
    def delete(self, work_experience: WorkExperience):
        pass

    @abstractmethod
    def get_by_id(self, work_experience_id: int):
        pass

    @abstractmethod
    def get_all(self, user_id: int):
        pass
