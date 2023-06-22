#!/usr/bin/python3
""" module definition comes here """
import json
import os
import csv
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file """
        file = type(list_objs[0]).__name__ + ".json"
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_data = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        else:
            list_obj = json.loads(json_string)
            return list_obj

    @classmethod
    def create(cls, **dictionary):
        """reurns an instance with all attributes set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        class_name = cls.__name__ + ".json"
        if not os.path.exists(class_name):
            return []
        else:
            with open(class_name) as f:
                j_string = f.read()
                string = cls.from_json_string(j_string)
            return [cls.create(**ob) for ob in string]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=keys)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.speed(0)
    
        for rectangle in list_rectangles:
            rectangle.draw()
    
        for square in list_squares:
            square.draw()
    
        turtle.done()
