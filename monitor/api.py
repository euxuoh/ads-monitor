"""
doc
"""
from flask_restful import Api
from flask_restful.utils import cors

from . import app
from monitor.resource.user import Hello


api = Api(app)
api.decorators = [cors.crossdomain(origin='*')]

api.add_resource(Hello, '/hello')
