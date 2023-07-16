from models.user_table import User_Registration_form
from configurations.config import session

from flask import Flask, request, jsonify
from flask_restful import Api

from Api.db_operation import is_userpwd_valid,is_user_valid, is_usermail_valid, is_userphone_valid

from utilis.reusable import *

app = Flask(__name__)



@app.route('/create-user', methods=['post'])
def create_user():
    """
    Creates a new user
    :return: Response as a dict
    """
    user_data = request.get_json()
    print(f"User data is---: {user_data}")

    if not is_user_valid(user_data.get('fname') + user_data.get('lname')):
        if is_userpwd_valid(user_data['password'], user_data.get('cpassword')):
            if not is_usermail_valid(user_data['mail']):
                if not is_userphone_valid(user_data['ph']):
                    try:
                        record = User_Registration_form(name=user_data.get('fname') + user_data.get('lname'),
                                                        fname=user_data.get('fname'),
                                                        lname=user_data.get('lname'),
                                                        date=user_data.get('date'),
                                                        password=user_data.get('password'),
                                                        cpassword=user_data.get('cpassword'),
                                                        mail=user_data.get('mail'),
                                                        ph=user_data.get('ph'),
                                                        add=user_data.get('add'),
                                                        category=user_data.get('category'))
                        session.add(record)
                        session.commit()
                        return success_response(f"User {user_data['fname']+user_data['lname']} Created successfully")
                    except Exception as err:
                        print(f"Error occurred is --- {err}")
                        session.rollback()
                        return failure_response(f"Database operation failed reason is --- {err}")
                else:
                    return failure_response(f"User {user_data['ph']} already exists")
            else:
                return failure_response(f"User {user_data['mail']} already exists")
        else:
            return failure_response(f"Password and Confirm password doesn't match")
    else:
        return failure_response(f"Username {user_data.get('fname') + user_data.get('lname')} already exist")


@app.route('/get-user-details', methods=['GET'])
def get_all_user_details():
    result = []
    try:
        result = session.query(User_Registration_form).all()
    except Exception as err:
        print(f"Error occurred is--- {err}")
    results_dict = [item.__dict__ for item in result]
    print(f"Result : {result}")
    print(f"Result to Dictionary : {results_dict}")
    for item in results_dict:
        del item['_sa_instance_state']
        print(f"Cleaned Dictionary is --- {results_dict}")
    if results_dict:
        return success_response(results_dict)
    else:
        return failure_response(f"{results_dict} Does not exist")


@app.route('/single-user', methods=['GET'])
def single_user():
    result = []
    user_selection = request.args.get('name')
    try:
        result = session.query(User_Registration_form).filter(User_Registration_form.name == user_selection).all()

    except Exception as err:
        print(f"Error occurred is {err}")
    results_dict = [item.__dict__ for item in result]
    print(f"Result : {result}")
    print(f"Result to Dict : {results_dict}")

    for item in results_dict:
        del item['_sa_instance_state']
    print(f"Cleaned Dict - {results_dict}")
    if results_dict:
        return success_response(results_dict)
    else:
        return failure_response(f"User name {user_selection} doesn't exist")


@app.route('/update-user-table', methods=['PATCH'])
def updated_user_table():
    data = request.get_json()
    print(f"Data is : {data}")
    if not is_user_valid(data.get('fname') + data.get('lname')):
        return failure_response(f"{data.get('fname') + data.get('lname')} User doesn't exist")
    try:
        session.query(User_Registration_form).filter(User_Registration_form.name == data.get('fname') + data.get('lname')).update(data)
        session.commit()
        return success_response(f"{data.get('fname') + data.get('lname')} user data has been updated with {data['category']}")
    except Exception as err:
        session.rollback()
        return failure_response(f"Unable to update User {data.get('fname') + data.get('lname')} Reason is:{err}")


@app.route('/delete-user', methods=['DELETE'])
def delete_user():
    '''
    This function is updated
    :return: 
    '''
    data = request.get_json()
    print(f"Data is : {data}")
    if not is_user_valid(data.get('fname') + data.get('lname')):
        return failure_response("{data.get('fname') + data.get('lname')} User doesn't exist")
    try:
        session.query(User_Registration_form).filter(User_Registration_form.name == data.get('fname') + data.get('lname')).delete()
        session.commit()
        return success_response(f"{data.get('fname') + data.get('lname')} User has been deleted")
    except Exception as err:
        session.rollback()
        return failure_response(f"Unable to delete User {data.get('fname') + data.get('lname')} Reason is:{err}")


app.run()
