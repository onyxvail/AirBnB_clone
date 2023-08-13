#!/usr/bin/python3
"""[User class]
"""
from models.base_model import BaseModel


class User(BaseModel):
    """[User]

    Args:
        BaseModel ([class]): [class inherited by User]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
