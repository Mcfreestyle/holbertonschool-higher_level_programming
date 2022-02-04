#!/usr/bin/python3
"""This module supplies the ``Base`` class
"""
import json


class Base:
    """Definiion of the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the objects

        Args:
            id = id of the object
        """

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        with open(filename, "w", encoding="UTF-8") as file:
            filecontent = cls.to_json_string(list_dictionaries)
            file.write(filecontent)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string"""
        if json_string is None or json_string == "":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        according dictionary
        """

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return (obj)
