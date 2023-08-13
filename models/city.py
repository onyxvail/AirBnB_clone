#!/usr/bin/python3
"""[City class]
"""
from models.base_model import BaseModel


class City(BaseModel):
    """[City]

    Args:
        BaseModel ([class]): [class that inherited by City]
    """
    state_id = ""
    name = ""
