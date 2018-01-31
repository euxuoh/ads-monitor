"""
doc
"""
import os
from sqlite3 import dbapi2 as sqlite3

from contextlib import closing
from flask import Flask

app = Flask(__name__)


class Config(object):
    """
    doc
    """
    DATABASE = os.path.join(app.root_path, 'monitor.db')

    JOBS = [
        {
            'id':'job1',
            'func':'flask-ap:test_data',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week':"mon-fri",
                'hour':'0-23',
                'minute':'0-11',
                'second': '*/5'
            }
        }
    ]

    SCHEDULER_API_ENABLED = True

app.config.from_object('Config')


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    db = connect_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


from .api import *
