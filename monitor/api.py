"""
doc
"""
from flask import request

from . import app
from .service.auth import check_user


@app.route('/adduser', methods=['POST'])
def add_user():
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    name = request.args.get('name', '')
    passwd = request.args.get('passwd', '')
    if check_user(name, passwd):
        return error


@app.route('/')
def hello():
    """
    test
    """
    return 'hello'

