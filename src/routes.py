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
from .Forum.ForumController import ForumController
from .ForumDiscussion.ForumDiscussionController import ForumDiscussionController
from .Service.ServiceController import ServiceController
from .ServiceImage.ServiceImageController import ServiceImageController
from .Publication.PublicationController import PublicationController
from.PublicationImage.PublicationImageController import PublicationImageController
from .PublicationComment.PublicationCommentController import PublicationCommentController
from .PublicationLike.PublicationLikeController import PublicationLikeController
from .Image.ImageController import ImageController
from .Messager.Message.MessageController import MessageController
from .Messager.Room.RoomController import RoomController
from .Messager.RoomUser.RoomUserController import RoomUserController
from .Company.CompanyController import CompanyController
from .Friend.FriendController import FriendController
from .Notification.NotificationController import NotificationController
from .Group.GroupController import GroupController
from .GroupInvite.GroupInviteController import GroupInviteController
from .Email.EmailController import EmailController
from .RestorePassword.RestorePasswordController import RestorePasswordController
from .Lang.LangController import LangController
from .Complaint.ComplaintController import ComplaintController
from .File.FileController import FileController

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
api.add_resource(ForumController, "/forum")
api.add_resource(ForumDiscussionController, "/forum_discussion")
api.add_resource(ServiceController, "/service")
api.add_resource(ServiceImageController, "/service_image")
api.add_resource(PublicationController, "/publication")
api.add_resource(PublicationImageController, "/publication_image")
api.add_resource(PublicationCommentController, "/publication_comment")
api.add_resource(PublicationLikeController, "/publication_like")
api.add_resource(ImageController, "/image")
api.add_resource(RoomController, "/room")
api.add_resource(MessageController, "/message")
api.add_resource(CompanyController, "/company")
api.add_resource(RoomUserController, "/room_user")
api.add_resource(FriendController, "/friend")
api.add_resource(NotificationController, "/notification")
api.add_resource(GroupController, "/group")
api.add_resource(GroupInviteController, "/group_invite")
api.add_resource(EmailController, "/email")
api.add_resource(RestorePasswordController, "/restore_password")
api.add_resource(LangController, "/lang")
api.add_resource(ComplaintController, "/complaint")
api.add_resource(FileController, "/file")
