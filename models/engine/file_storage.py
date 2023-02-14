#!/usr/bin/python3

"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:
"""

import json

class FileStorage():
    """
    args :
    __file_path: string - path to the JSON file (ex: file.json)    __objects: dictionary - empty but will store all objects by <class name>.id
    save(self): serializes __objects to the JSON file
    """

    __file_path = "my_file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = self.__class__.name + '.' + self.id
        self.__objects[key] = obj

    def save(self):
        my_dict = self.__objects
        {k : v.to_dict for k, v in my_dict.items()}
        with open(self.__file_path, 'w', encoding = 'utf-8') as f:
                json.dump(my_dict, f)
    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding = 'utf-8')as f:
                load_file = json.load(f)
                for first_v in load_file.values():
                    if k == "__class__":
                        save = k
                        del load_file[k]
                    self.new(eval(k)(**first_v) )
        except FileNotFoundError:
            return
