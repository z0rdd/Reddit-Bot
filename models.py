from flask.ext.sqlalchemy import SQLAlchemy
from webapp import app


db = SQLAlchemy(app)


class Stats(db.Model):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.String(15))
    author = db.Column(db.String(120), unique=True)
    hit_count = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True))

    def __init__(self, comment_id, author, hit_count, date):
        self.comment_id = comment_id
        self.author = author
        self.hit_count = hit_count
        self.date = date

