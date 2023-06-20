#!/usr/bin/python3
""" test for class Square """
import unittest
from models.square import Square


class TestModuleDocstring(unittest.TestCase):
    """ test square that inherits from rectangle"""

    def test_module_docstring(self):
        """test docstring"""
        docstring = Square.__doc__
        self.assertIn("class Square that inherits from Rectangle", docstring)
        self.assertIn("returns the square string", docstring)
        self.assertIn("sets the value of size", docstring)

    def test_size_property(self):
        """ test size property"""
        square = Square(10, 0, 0)
        self.assertEqual(square.size, 10)
        square.size = 20
        self.assertEqual(square.size, 20)

    def test_negative_size(self):
        """ test negative size"""
        with self.assertRaises(ValueError):
            square = Square(-10, 0, 0)
        with self.assertRaises(ValueError):
            square = Square(10, -20, 0, 0)


if __name__ == '__main__':
    unittest.main()
