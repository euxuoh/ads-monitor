from monitor.model.user import User
from monitor.model.account import Account


def add_user(name=None, passwd=None):
    if name and passwd:
        user = Account(name, passwd)
        user.save()


def add_account(name=None, passwd=None):
    if name and passwd:
        user = Account(name, passwd)
        user.save()


def check_user(id=None, passwd=None):
    if id and passwd:
        user = User.query.filter_by(id=id).first()
        return True if passwd == user.title else False
