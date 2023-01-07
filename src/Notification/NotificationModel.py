from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Notification(Model, db.Model):
    friend_id = db.Column(db.Integer, db.ForeignKey("friend.id"))
    friend = relationship("Friend")

    vacancy_offer_id = db.Column(db.Integer, db.ForeignKey("vacancy_offer.id"))
    vacancy_offer = relationship("VacancyOffer")

    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    team = relationship("Team")

    user_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User", uselist=False)