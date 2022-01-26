#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the test methods"""

    def test_docstring_class(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_int(self):
        self.assertEqual(max_integer([-4, -1, -2]), -1)

    def test_positive_float(self):
        self.assertEqual(max_integer([2.456, 6.1, 5.2]), 6.1)

    def test_negative_float(self):
        self.assertEqual(max_integer([-2.456, -6.1, -5.2]), -2.456)

    def test_posit_negat_zeros(self):
        self.assertEqual(max_integer([0.3, -0.5, -0.1]), 0.3)

    def test_unique_item(self):
        self.assertEqual(max_integer([45]), 45)

    def test_strings(self):
        self.assertEqual(max_integer(['k', 'r', 'b', 'A']), 'r')

    def test_strings_int(self):
        self.assertRaises(TypeError, max_integer, ["hi", 5, "hello"])
