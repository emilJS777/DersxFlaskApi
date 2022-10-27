from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Forum(db.Model, Model):
    title = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(480), nullable=False)

    rubric_id = db.Column(db.Integer, db.ForeignKey("rubric.id"))
    rubric = relationship("Rubric")
    forum_discussions = relationship("ForumDiscussion")

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
