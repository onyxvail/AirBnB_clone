#!/usr/bin/python3
"""
    BaseModel module
"""
import uuid
from datetime import datetime


class BaseModel():
    """
        Base model class forall the common methods
    """
    def __init__(self, *args, **kwargs):
        """
            Initializer

            id: public instance attribute

        """
        from models import storage
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
            Human readable format
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns the dictionary format
        """
        dct = dict(self.__dict__)
        dct["created_at"] = dct["created_at"].isoformat()
        dct["updated_at"] = dct["updated_at"].isoformat()
        dct["__class__"] = self.__class__.__name__
        return dct
