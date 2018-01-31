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

app.logger.addHandler(handler)

app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(app.root_path, 'monitor.db')

from .api import *
