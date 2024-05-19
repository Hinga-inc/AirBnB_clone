#!/usr/bin/python3


from models.base_model import BaseModel

class User(BaseModel):
    """ This represents a user
    """
    email = "" # users email
    password = "" # User password
    first_name = "" # first name of the user
    last_name = "" #last name for user