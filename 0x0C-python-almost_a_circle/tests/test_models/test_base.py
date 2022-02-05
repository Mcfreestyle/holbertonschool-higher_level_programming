#!/usr/bin/python3
"""This modules supplies differents tests to the Base class
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseAttr(unittest.TestCase):
    """Tests the attributes of the Base Class"""

    def test_pep8(self):
        """Tests pep8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base.py"])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
        )

    def test_init_id_without_arg(self):
        """Tests creation of object without passed argument"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_init_id_with_arg(self):
        """Tests creation of object with passed argument"""
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(98).id, 98)

    def test_order_id(self):
        """Tests order of objects ids"""
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(34).id, 34)
        self.assertEqual(Base().id, 4)


class TestBaseToJsonString(unittest.TestCase):
    """Tests for ``to_json_string`` method"""
    def test_list_dicts(self):
        """Test with list of dictionaries"""
        json_list = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertEqual(json_list, '[{"id": 1}, {"id": 2}]')

    def test_empty_list(self):
        """Test with empty list"""
        json_list = Base.to_json_string([])
        self.assertEqual(json_list, "[]")

    def test_None(self):
        """Test with None argument"""
        json_list = Base.to_json_string(None)
        self.assertEqual(json_list, "[]")


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for ``save_to_file`` method """
    def test_objs_list(self):
        """Test with list of objects"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_None(self):
        """Test with empty list"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            result = file.read()
        self.assertEqual(result, "[]")

    def test_wrong_use(self):
        """Test the use of the method with the Base Class"""
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base(), Base()])


class TestBaseFromJsonString(unittest.TestCase):
    """Tests for the ``from_json_string`` method"""
    def test_json_string(self):
        """Test with json string as argument"""
        json_list = '[{"id": 1, "width": 10, "height": 4}]'
        obj_list = Base.from_json_string(json_list)
        self.assertEqual(obj_list, [{"id": 1, "width": 10, "height": 4}])
        self.assertTrue(type(obj_list) is list)

    def test_empty_str(self):
        """Test with empty string"""
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])
        self.assertTrue(type(obj_list) is list)

    def test_None(self):
        """Test with None as argument"""
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])
        self.assertTrue(type(obj_list) is list)


class TestBaseCreate(unittest.TestCase):
    """Tests for the ``create`` method"""
    def test_Rectangle(self):
        """Test with Rectangle class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(type(r2) is Rectangle)
        self.assertFalse(r1 is r2)

    def test_Square(self):
        """Test with Square class"""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertTrue(type(s2) is Square)
        self.assertFalse(s1 is s2)

    def test_Base(self):
        """Test with Base Class"""
        with self.assertRaises(UnboundLocalError):
            s1 = Square(3, 5, 1)
            s1_dictionary = s1.to_dictionary()
            b = Base.create(**s1_dictionary)

    def test_dictionary(self):
        """Test with dictionary as argument"""
        with self.assertRaises(TypeError):
            Rectangle.create({"id": 1, "width": 10, "height": 3})


class TestBaseLoadFromFile(unittest.TestCase):
    """Test for the ``load_from_file`` method"""
    def test_Rectangle(self):
        """Test with Rectangle class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertTrue(type(list_rectangles_output) is list)
        for rect in list_rectangles_output:
            self.assertTrue(type(rect) is Rectangle)

    def test_Square(self):
        """Test with Square class"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(os.path.exists("Square.json"))
        self.assertTrue(type(list_squares_output) is list)
        for square in list_squares_output:
            self.assertTrue(type(square) is Square)
