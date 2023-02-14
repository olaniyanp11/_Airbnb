#!/usr/bin/python3
"""
 a class BaseModel that defines all common attributes/methods for other classes
"""
from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime


class BaseModel():

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
                storage.new()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
    def save(self):
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        mydict = self.__dict__
        mydict["__class__"] = f"{self.__class__.__name__}"
        mydict["created_at"] =  self.created_at.isoformat()
        mydict["updated_at"] =  self.updated_at.isoformat()
        return mydict
