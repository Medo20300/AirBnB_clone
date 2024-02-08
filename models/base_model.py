#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            - *args: list of arguments
            - **kwargs: dict of keys and vals arguments
            """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, time_format)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """Update <updated_at> with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance
         >>Includes the key/value pair __class__ representing
        the class name of the object.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
