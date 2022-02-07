#!/usr/bin/python3
"""This modules supplies differents tests to the Rectangle class"""
import unittest
import pycodestyle

import sys
from contextlib import contextmanager
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle


class TestRectangleCreation(unittest.TestCase):
    """Tests the attributes of the Rectangle Class"""

    def test_pep8(self):
        """Tests pep8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/rectangle.py"])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
        )

    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        """Tests the instance of a rectangle"""
        self.assertTrue(isinstance(Rectangle(1, 1), Rectangle))
        self.assertEqual(type(Rectangle(4, 5)), Rectangle)

    def test_is_subclass(self):
        """Tests if a rectangle is a subclass of Base"""
        self.assertTrue(issubclass(type(Rectangle(1, 1)), Base))

    def test_wrong_init(self):
        """Test for creation of rectangle with expected arguments"""
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (1))
        self.assertRaises(TypeError, Rectangle, (1, 1, 1, 1, 1, 1))


class TestRectangleAttributes(unittest.TestCase):
    """Tests the attributes of a rectangle"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_init(self):
        """Test if the object catch the correct attributes"""
        r = Rectangle(4, 5, 1, 2, 17)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 17)

    def test_input_not_integer(self):
        """Test if input is not a integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2 = Rectangle(10, 2)
            r2.height = {}

    def test_width_height_less_or_equal_0(self):
        """Test if width or height is <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2 = Rectangle(1, 1)
            r2.height = -2

    def test_x_y_less_0(self):
        """Test if x or y is < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(1, 1, -2, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2 = Rectangle(1, 1, 1, 1)
            r2.y = -2

    def test_private(self):
        """Tests if a rectangle attribute is private"""
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)
        with self.assertRaises(AttributeError):
            r1.__x


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_return(self):
        """Tests the correct return of the method"""
        str1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(), str1)
        str2 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(Rectangle(5, 5, 1).__str__(), str2)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_area(self):
        """Tests the correct area of the rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_wrong_args(self):
        """Test with incorrect arguments"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(2, -3)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_correct_print(self):
        """Tests the correct print"""
        r1 = Rectangle(3, 2)
        with self.captured_output() as (out, err):
            r1.display()
        output = out.getvalue()
        self.assertEqual(output, "###\n###\n")

        r2 = Rectangle(2, 3, 2, 2)
        with self.captured_output() as (out, err):
            r2.display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")

    def test_invalid_args(self):
        """Tests with invalid arguments"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(2, 3, 0, -5)
            r1.display()


class TestRectangleUpdate(unittest.TestCase):
    """Tests for the update method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_without_args(self):
        """Tests the update of rectangle attributes without arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_no_keyword_args(self):
        """Tests the update of rectangle attributes with no-keyword args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_more_than_5_args(self):
        """Tests with more than 5 *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(2, 3, 1, 1, 13, 4, 9)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/13 - 3/1")

    def test_invalid_args(self):
        """Tests with invalid *args"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(2, "3")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(2, 3, -4)

    def test_key_worded_args(self):
        """Tests the update of rectangle attributes with key-worded args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/3 - 4/2")

    def test_more_than_5_kwargs(self):
        """Tests with more than 5 kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, width=3, height=4, id=98, y=3, per=45, area=12)
        self.assertEqual(str(r1), "[Rectangle] (98) 1/3 - 3/4")

    def test_invalid_kwargs(self):
        """Tests with invalid kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(x=3, y="6")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(height=2, y=3, width=-5)

    def test_no_and_keyword_args(self):
        """Tests with no-keyword and key_worded arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 4, height=1)
        self.assertEqual(str(r1), "[Rectangle] (3) 10/10 - 4/10")

        # self.assertRaises(SyntaxError, r1.update, y=7, width=9, 2, 1)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_dict(self):
        """Tests the correct return of the rectangle dictionar"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dict, d)
        self.assertTrue(type(r1_dict) is dict)
