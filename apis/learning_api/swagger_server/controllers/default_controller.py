import connexion
import json
import os
import random
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server import util

# Loading the data
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/../data/users.json', 'r') as f:
    USER_DATA = json.load(f)


def random_get():  # noqa: E501
    """Get information about a random user.

     # noqa: E501


    :rtype: InlineResponse200
    """
    return USER_DATA[random.randint(0, len(USER_DATA) - 1)]


def user_get(firstname=None, lastname=None, gender=None, page=None):  # noqa: E501
    """Get information about specific users.

     # noqa: E501

    :param firstname: The user&#x27;s first name.
    :type firstname: str
    :param lastname: The user&#x27;s last name.
    :type lastname: str
    :param gender: The gender of the user.
    :type gender: str
    :param page: The page (10 results per page)
    :type page: int

    :rtype: List[InlineResponse200]
    """

    try:
        filtered_users = USER_DATA
        if firstname:
            filtered_users = [
                user
                for user in filtered_users
                if user['first_name'] == firstname
            ]
        if lastname:
            filtered_users = [
                user
                for user in filtered_users
                if user['last_name'] == lastname
            ]
        if gender:
            filtered_users = [
                user
                for user in filtered_users
                if user['gender'] == gender
            ]
    
        # pagination
        filtered_users = filtered_users[((page - 1) * 10):(page * 10)]
    
    except Exception as e:
        return {"message": str(e)}, 400

    return filtered_users
