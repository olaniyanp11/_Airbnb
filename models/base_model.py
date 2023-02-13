#!/usr/bin/python3
"""
 a class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
class BaseModel():

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for lil_dict in self.__dict__:
                if lil_dict == "__class__":
                    continue
                elif lil_dict == ["created_at"] or i == ["updated_at"]:
                    lil_dict = lil_dict.fromisoformat()
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
    def save(self):
        updated_at = datetime.now()

    def to_dict(self):
        mydict = self.__dict__
        mydict["__class__"] = f"{self.__class__.__name__}"
        mydict["created_at"] =  self.created_at.isoformat()
        mydict["updated_at"] =  self.updated_at.isoformat()
        return mydict
