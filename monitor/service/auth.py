from monitor.model.user import User


def check_user(id=None, passwd=None):
    if id and passwd:
        user = User.query.filter_by(id=id).first()
        return True if passwd == user.title else False
