#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2018/1/31
"""
from flask_restful import Resource
from flask_restful import reqparse

from monitor.service.auth import add_user
from monitor.service.auth import add_account


class Hello(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('name', type=str)
        self.parse.add_argument('passwd', type=str)
        super(Hello, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        name = args.get('name', '')
        passwd = args.get('passwd', '')

    def post(self):
        args = self.parse.parse_args()
        name = args.get('name', '')
        passwd = args.get('passwd', '')
        print(name, passwd)
        add_account(name, passwd)


if __name__ == "__main__":
    pass
