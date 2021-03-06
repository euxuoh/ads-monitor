"""
doc
"""
import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# 日志配置
handler = RotatingFileHandler('api.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
handler.setLevel(logging.INFO)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'monitor.db')
    JOBS = [
        {
            'id': 'job1',
            'func': 'monitor.scheduler.jobs:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    SCHEDULER_API_ENABLED = True


app.logger.addHandler(handler)
app.config.from_object(Config)

from .api import *
from .scheduler.jobs import scheduler
