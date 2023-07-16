from models.user_table import User_Registration_form
from configurations.config import session


def is_user_valid(name):
    """
    This function return True if product is valid otherwise false
    """
    result = session.query(User_Registration_form).filter(User_Registration_form.name == name).all()
    if result:
        return True
    else:
        return False


def is_usermail_valid(mail):
    result = session.query(User_Registration_form).filter(User_Registration_form.mail == mail).all()
    if result:
        return True
    else:
        return False


def is_userphone_valid(phone):
    result = session.query(User_Registration_form).filter(User_Registration_form.phone == phone).all()
    if result:
        return True
    else:
        return False


def is_userpwd_valid(password):
    result = session.query(User_Registration_form).filter(User_Registration_form.password == password).all()
    if result:
        return True
    else:
        return False

