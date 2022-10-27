from sqlalchemy.orm import relationship
from datetime import datetime
from src import db
from src.__Parents.Model import Model


class ForumDiscussion(db.Model, Model):
    description = db.Column(db.Text, nullable=False)

    forum_id = db.Column(db.Integer, db.ForeignKey("forum.id"))
    forum = relationship("Forum")

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")

    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
