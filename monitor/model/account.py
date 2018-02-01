#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2018/2/1
"""
from . import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text

    def save(self):
        db.session.add(self)
        db.session.commit()
        print('Account save')
        return self
