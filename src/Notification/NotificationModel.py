from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Notification(Model, db.Model):
    friend_id = db.Column(db.Integer, db.ForeignKey("friend.id"))
    friend = relationship("Friend")

    vacancy_offer_id = db.Column(db.Integer, db.ForeignKey("vacancy_offer.id"))
    vacancy_offer = relationship("VacancyOffer")

    group_invite_id = db.Column(db.Integer, db.ForeignKey("group_invite.id"))
    group_invite = relationship("GroupInvite")

    publication_comment_id = db.Column(db.Integer, db.ForeignKey("publication_comment.id"))
    publication_comment = relationship("PublicationComment")

    user_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User", uselist=False)
