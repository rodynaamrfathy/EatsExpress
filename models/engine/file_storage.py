#!/usr/bin/python3
"""This is the file storage class for your system"""
import json
from models.base_model import BaseModel
from models.user import User
from models.restaurant import Restaurant
from models.review import Review
from models.order import Order
import shlex

# Class dictionary for mapping class names to classes
classes = {"BaseModel": BaseModel, "User": User, "Restaurant": Restaurant, "Review": Review, "Order": Order}

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value._class_ or cls == value._class.name_:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj._class.name_ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {key: obj.to_dict(save_fs=1) for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key, obj_data in jo.items():
                self._objects[key] = classes[obj_data["class_"]](**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj._class.name_ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or None if not found"""
        if cls not in classes.values():
            return None
        all_cls = self.all(cls)
        return all_cls.get(f"{cls._name_}.{id}")

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if not cls:
            return len(self.__objects)
        return len(self.all(cls))

#!/usr/bin/python3
"""This is the file storage class for your system"""
import json
from models.base_model import BaseModel
from models.user import User
from models.restaurant import Restaurant
from models.review import Review
from models.order import Order
import shlex

# Class dictionary for mapping class names to classes
classes = {"BaseModel": BaseModel, "User": User, "Restaurant": Restaurant, "Review": Review, "Order": Order}

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value._class_ or cls == value._class.name_:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj._class.name_ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {key: obj.to_dict(save_fs=1) for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key, obj_data in jo.items():
                self._objects[key] = classes[obj_data["class_"]](**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj._class.name_ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or None if not found"""
        if cls not in classes.values():
            return None
        all_cls = self.all(cls)
        return all_cls.get(f"{cls._name_}.{id}")

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if not cls:
            return len(self.__objects)
        return len(self.all(cls))