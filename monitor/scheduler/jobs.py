#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2018/2/1
"""
from flask_apscheduler import APScheduler

from .. import app


def job1(a, b):
    print(str(a) + str(b))


def spider():
    print('spider')


scheduler = APScheduler()
scheduler.init_app(app)
