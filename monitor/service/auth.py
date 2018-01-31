from monitor.model.user import User


def add_user(name=None, passwd=None):
    if name and passwd:
        user = User(name, passwd)
        user.save()


def check_user(id=None, passwd=None):
    if id and passwd:
        user = User.query.filter_by(id=id).first()
        return True if passwd == user.title else False
