#!/usr/bin/python3
"""This modules supplies differents tests to the Square class"""
import unittest
import pycodestyle

import sys
from contextlib import contextmanager
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareCreation(unittest.TestCase):
    """Tests the correct creation of a square"""

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
        """Tests the instance of a square"""
        self.assertTrue(isinstance(Square(4), Square))
        self.assertEqual(type(Square(4)), Square)

    def test_is_subclass(self):
        """Tests if a square is a subclass of Rectangle and Base"""
        self.assertTrue(issubclass(type(Square(1)), Rectangle))
        self.assertTrue(issubclass(type(Square(1)), Base))

    def test_wrong_init(self):
        """Test for creation of square with unexpected arguments"""
        self.assertRaises(TypeError, Square, ())
        self.assertRaises(TypeError, Square, (1, 1, 1, 1, 1))


class TestSquareAttributes(unittest.TestCase):
    """Tests the attributes of a square"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_init(self):
        """Test if the object catch the correct attributes"""
        s = Square(5, 1, 2, 17)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 17)

    def test_input_not_integer(self):
        """Test if input is not a integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s2 = Square(10, 2, 1)
            s2.size = {}

    def test_width_height_less_or_equal_0(self):
        """Test if width or height is <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s2 = Square(1, 1, 1)
            s2.size = -2

    def test_x_y_less_0(self):
        """Test if x or y is < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(1, -1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s2 = Square(1, 1, 1)
            s2.y = -2

    def test_private(self):
        """Tests if a square attribute is private"""
        s1 = Square(1, 1, 1)
        self.assertEqual(s1.id, 1)
        with self.assertRaises(AttributeError):
            s1.__x


class TestSquareStr(unittest.TestCase):
    """Tests for the __str__ method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_return(self):
        """Tests the correct return of the method"""
        str1 = "[Square] (12) 2/1 - 4"
        self.assertEqual(Square(4, 2, 1, 12).__str__(), str1)
        str2 = "[Square] (1) 5/1 - 5"
        self.assertEqual(Square(5, 5, 1).__str__(), str2)


class TestSquareArea(unittest.TestCase):
    """Tests for the area method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_area(self):
        """Tests the correct area of the square"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(8, 7, 0, 12)
        self.assertEqual(s2.area(), 64)

    def test_wrong_args(self):
        """Test with incorrect arguments"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(-3)


class TestSquareDisplay(unittest.TestCase):
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
        s1 = Square(3)
        with self.captured_output() as (out, err):
            s1.display()
        output = out.getvalue()
        self.assertEqual(output, "###\n###\n###\n")

        s2 = Square(2, 3, 2, 2)
        with self.captured_output() as (out, err):
            s2.display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n   ##\n   ##\n")

    def test_invalid_args(self):
        """Tests with invalid arguments"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1 = Square(2, 3, -5)
            s1.display()


class TestSquareUpdate(unittest.TestCase):
    """Tests for the update method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0
        self.s1 = Square(10, 10, 10)

    def test_without_args(self):
        """Tests the update of square attributes without arguments"""
        self.s1.update()
        self.assertEqual(str(self.s1), "[Square] (1) 10/10 - 10")

    def test_no_keyword_args(self):
        """Tests the update of square attributes with no-keyword args"""
        self.s1.update(89)
        self.assertEqual(str(self.s1), "[Square] (89) 10/10 - 10")

        self.s1.update(89, 2, 3, 4)
        self.assertEqual(str(self.s1), "[Square] (89) 3/4 - 2")

    def test_more_than_5_args(self):
        """Tests with more than 5 *args"""
        self.s1.update(2, 3, 1, 1, 13, 4, 9)
        self.assertEqual(str(self.s1), "[Square] (2) 1/1 - 3")

    def test_invalid_args(self):
        """Tests with invalid *args"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.update(2, "3")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(2, -4)

    def test_key_worded_args(self):
        """Tests the update of square attributes with key-worded args"""
        self.s1.update(size=1)
        self.assertEqual(str(self.s1), "[Square] (1) 10/10 - 1")

        self.s1.update(x=1, size=2, y=3)
        self.assertEqual(str(self.s1), "[Square] (1) 1/3 - 2")

    def test_more_than_5_kwargs(self):
        """Tests with more than 5 kwargs"""
        self.s1.update(x=1, size=3, id=98, y=3, per=45, area=9)
        self.assertEqual(str(self.s1), "[Square] (98) 1/3 - 3")

    def test_invalid_kwargs(self):
        """Tests with invalid kwargs"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.update(x=3, y="6")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(y=3, size=-5)

    def test_no_and_keyword_args(self):
        """Tests with no-keyword and key_worded arguments"""
        self.s1.update(3, 4, size=1)
        self.assertEqual(str(self.s1), "[Square] (3) 10/10 - 4")

        # self.assertRaises(SyntaxError, self.s1.update, y=7, size=9, 2, 1)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_correct_dict(self):
        """Tests the correct return of the square dictionary"""
        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        d = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, d)
        self.assertTrue(type(s1_dict) is dict)
