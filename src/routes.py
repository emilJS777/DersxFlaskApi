from src import api
from .Auth.AuthController import AuthController
from .User.UserController import UserController
from .Rubric.RubricController import RubricController
from .Category.CategoryController import CategoryController
from .Skill.SkillController import SkillController
from .WorkExperience.WorkExperienceController import WorkExperienceController
from .Gender.GenderController import GenderController
from .UserAbout.UserAboutController import UserAboutController
from .UserContact.UserContactController import UserContactController
from .UserImage.UserImageController import UserImageController
from .Vacancy.VacancyController import VacancyController
from .PaymentInterval.PaymentIntervalController import PaymentIntervalController
from .VacancyComment.VacancyCommentController import VacancyCommentController
from .VacancyOffer.VacancyOfferController import VacancyOfferController

api.add_resource(AuthController, "/auth")
api.add_resource(UserController, "/user")
api.add_resource(RubricController, "/rubric")
api.add_resource(CategoryController, "/category")
api.add_resource(SkillController, "/skill")
api.add_resource(WorkExperienceController, "/work_experience")
api.add_resource(GenderController, "/gender")
api.add_resource(UserAboutController, "/user_about")
api.add_resource(UserContactController, "/user_contact")
api.add_resource(UserImageController, "/user_image")
api.add_resource(VacancyController, "/vacancy")
api.add_resource(PaymentIntervalController, "/payment_interval")
api.add_resource(VacancyCommentController, "/vacancy_comment")
api.add_resource(VacancyOfferController, "/vacancy_offer")
