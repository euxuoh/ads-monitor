"""
doc
"""
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, name=None, passwd=None):
        self.title = name
        self.text = passwd

    def save(self):
        db.session.add(self)
        db.session.commit()
        print('save')
        return self

    def update(self):
        db.session.commit()
        return self
