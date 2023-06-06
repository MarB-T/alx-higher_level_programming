#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test for max_integer"""

    def test_ordered_list(self):
        """test for max value in an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_unordered_list(self):
        """test for unordered list"""
        self.assertEqual(max_integer([100, 40, 550, 120, 900, 3, 5]), 900)

    def test_floats(self):
        """test floating point numbers"""
        self.assertEqual(max_integer([10.2, 1.0, 30.2, 20, 30.5, 30.4, 30.3])
                                     , 30.5)
    def test_equal_max(self):
        """test when more than one max integer exist"""
        self.assertEual(max_integer([32, 87, 99, 56, 99]), 99)

    def test_negatives(self):
        """tests negative integers"""
        self.assertEqual(max_integer([-9, -67, -3, -87, -1]), -1)

    def test_single_list(self):
        """test for single element"""
        s = [2]
        self.assertEqual(max_integer(s), 2)

    def test_empty_argument(self):
        """test for empty element"""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """test string"""
        name = "Moraa"
        self.assertEqual(max_integer(name), 'r')
