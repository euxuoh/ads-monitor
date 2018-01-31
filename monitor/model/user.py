"""
doc
"""
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, id, title=None, text=None):
        self.id = id
        self.title = title
        self.text = text

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
